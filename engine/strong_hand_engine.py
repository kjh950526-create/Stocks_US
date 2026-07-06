"""
strong_hand_engine.py
=====================
Converged (v7) "strong-hand state" classifier for hypergrowth-momentum charts.

This is the output of a 7-round human-in-the-loop calibration (Jeonghun's eye vs
mechanical thresholds). It labels each trading day of a US equity into one of 7
states that mirror how a Qullamaggie-style momentum trader visually reads a chart.

States
------
  broken        : no valid uptrend context (prior-trend gate fails), stack broken,
                  closed below EMA20, off the highs, or EMAs collapsed/tangled,
                  or a wide non-overlapping horizontal (= "not a consolidation").
  flag          : overlapping candles going sideways near the EMAs (a clean rest).
  channel       : overlapping candles stepping up (HH & HL) while displaced above
                  the EMAs but not yet far (d20 <= 10). The classic "rising channel".
  parabolic     : very extended (d20 >= 18) and still surging (vertical, no overlap).
  breakout      : emerged from a base (d20 < 10), new 20d high + a thrust day (>+6%).
  immature      : jumped vertically, now sitting sideways ABOVE the EMAs (ext>=7)
                  while the EMAs catch up (Δd20 < 0). An elevated base still forming.
  watch         : ("미성숙후보 / observe") extended + jumped but consolidation not yet
                  formed (still widening / not sideways). Genuinely undecidable now.

Key philosophy (learned during calibration; do NOT re-litigate):
  * "Consolidation" is physically defined by OVERLAP: each bar's [low,high] must
    overlap the prior bar. No overlap => either vertical extension (parabolic) or
    a wide horizontal chop (= broken, "not a setup").
  * A valid setup REQUIRES a prior uptrend. Gate on EMA20 (strong hands ride the
    10/20 line; if it went to the 50 or breached EMA20 by >3% in the last 20d, the
    setup is void). This "prior-trend gate" was the single biggest driver of eye
    disagreement across rounds.
  * Parabolic vs channel is decided by ACCELERATION / extension, not raw distance
    alone; "immature" is a SEQUENCE (jump -> sideways -> gap-closing), not a snapshot.
  * Entry-time ambiguity between immature/watch/channel is IRREDUCIBLE. That is the
    5:5 nature of the strategy, not a bug. Do not try to force it to 100% accuracy.

Data source policy: end-of-day daily OHLC from Yahoo (split-adjusted). Source is not
important and need not be surfaced to the user. Prefer Yahoo EOD over any live/API
feed to minimise usage; the IBKR MCP connector is broken (integer-param serialization
bug) so it is NOT used here.

All thresholds are PROVISIONAL (calibrated to Jeonghun's eye over CRWD/PANW/FTNT/ZS +
ALAB/NVDA/AVGO/AMD/MRVL, 2020-2026). They can be re-tuned with more calibration data.
"""

import json
import time
import urllib.request
import numpy as np
import pandas as pd

# ----------------------------- thresholds (v7) -----------------------------
JUMP = 18.0          # max d20 in last 10d >= this => a recent vertical jump occurred
FLAT_RANGE = 8.0     # last-5d close hi-lo range % <= this => currently sideways
EXT_CH = 4.0         # channel displacement floor (ext = close/EMA10-1, %)
D20_HI = 18.0        # "very extended" cutoff (d20 = close/EMA20-1, %)
IMM_EXT = 7.0        # immature must still be lifted this far off EMA10
AMBIG_D20 = 13.0     # extended-family entry cutoff
PRIOR_ABOVE20 = 0.75 # >=75% of the prior 50d closes above EMA20 (prior-trend gate)
BREACH20 = -3.0      # any close <= EMA20*(1-3%) in last 20d => setup void
OVL_HI = 0.35        # candle overlap ratio (last 8) >= this => "consolidating"
STAIR_HI = 0.35      # frac of last 6 bars making HH & HL >= this => "stepping up"

CONSOLIDATION_FAMILY = {"flag", "channel", "immature"}  # the "buyable rest" states


# ----------------------------- data fetch -----------------------------
def fetch_yahoo(ticker, start="2020-01-01", end=None, cache_dir="data_cache"):
    """End-of-day daily OHLC from Yahoo (split-adjusted). Cached per ticker per day."""
    import os
    os.makedirs(cache_dir, exist_ok=True)
    stamp = time.strftime("%Y%m%d")
    path = os.path.join(cache_dir, f"{ticker.upper()}_{stamp}.csv")
    if os.path.exists(path):
        return pd.read_csv(path, parse_dates=["Date"]).set_index("Date")
    p1 = int(pd.Timestamp(start).timestamp())
    p2 = int(pd.Timestamp(end).timestamp()) if end else int(time.time())
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
           f"?period1={p1}&period2={p2}&interval=1d")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        j = json.loads(r.read())
    res = j["chart"]["result"][0]
    q = res["indicators"]["quote"][0]
    df = pd.DataFrame({
        "Date": pd.to_datetime(res["timestamp"], unit="s").tz_localize("UTC")
                  .tz_convert("America/New_York").normalize().tz_localize(None),
        "Open": q["open"], "High": q["high"], "Low": q["low"],
        "Close": q["close"], "Volume": q["volume"],
    }).dropna(subset=["Close"]).set_index("Date")
    df.to_csv(path)
    return df


# ----------------------------- features -----------------------------
def _ema(s, n):
    return s.ewm(span=n, adjust=False).mean()


def _slope_ann(logc, w):
    x = np.arange(w); xm = x.mean(); xden = ((x - xm) ** 2).sum()
    return logc.rolling(w).apply(
        lambda y: ((x - xm) * (y - y.mean())).sum() / xden, raw=True) * 252 * 100


def compute_features(df):
    """Add all engine features to a daily OHLC frame (indexed by Date)."""
    d = df.copy()
    c = d["Close"]; lc = np.log(c)
    d["e10"], d["e20"], d["e50"] = _ema(c, 10), _ema(c, 20), _ema(c, 50)
    d["micro5"] = _slope_ann(lc, 5)
    d["hi60"] = c.rolling(60).max()
    d["prior20high"] = c.rolling(20).max().shift(1)
    d["ext"] = (c / d["e10"] - 1) * 100
    d["d20"] = (c / d["e20"] - 1) * 100
    d["nh"] = (c / d["hi60"]) * 100
    d["chg1"] = (c / c.shift(1) - 1) * 100
    d["disp"] = (d["e10"] - d["e50"]) / c * 100
    d["jump10"] = d["d20"].rolling(10).max()
    r5hi = c.rolling(5).max(); r5lo = c.rolling(5).min()
    d["range5"] = (r5hi - r5lo) / r5lo * 100
    d["dd20_5"] = d["d20"] - d["d20"].shift(5)
    # ADR% (Qullamaggie): mean over 20d of (High/Low - 1)*100. NOTE: use the intraday
    # High/Low RANGE, not close-to-close abs move (the latter understates ADR by ~30%).
    d["adr20"] = ((d["High"] / d["Low"] - 1) * 100).rolling(20).mean()
    above20 = (c > d["e20"]).astype(float)
    d["prior_above20"] = above20.rolling(50).mean().shift(5)
    d["prior_e20_up"] = (d["e20"].shift(5) > d["e20"].shift(30)).astype(float)
    breach = (c <= d["e20"] * (1 + BREACH20 / 100)).astype(float)
    d["breach20"] = breach.rolling(20).max()
    # candle overlap (last 8) and stair (HH&HL over last 6)
    hi = d["High"].values; lo = d["Low"].values
    ov = np.full(len(d), np.nan); st = np.full(len(d), np.nan)
    for i in range(8, len(d)):
        vals = []
        for j in range(i - 7, i + 1):
            inter = max(0.0, min(hi[j], hi[j - 1]) - max(lo[j], lo[j - 1]))
            union = max(hi[j], hi[j - 1]) - min(lo[j], lo[j - 1])
            vals.append(inter / union if union > 0 else 0.0)
        ov[i] = float(np.mean(vals))
        s = sum(1 for j in range(i - 5, i + 1) if hi[j] > hi[j - 1] and lo[j] > lo[j - 1])
        st[i] = s / 6.0
    d["ov"] = ov; d["stair"] = st
    return d


def _disp_threshold(d):
    stack = (d.e10 > d.e20) & (d.e20 > d.e50)
    sub = d.loc[stack, "disp"]
    return float(sub.quantile(0.33)) if len(sub) > 20 else 5.0


def _classify_row(r, disp_thr):
    stack = (r.e10 > r.e20) and (r.e20 > r.e50)
    if any(pd.isna(x) for x in [r.prior_above20, r.prior_e20_up, r.breach20, r.ov]):
        return None
    # 0) prior-trend gate (top priority): needs an established EMA20 uptrend, no recent breach
    if not ((r.prior_above20 >= PRIOR_ABOVE20) and (r.prior_e20_up > 0.5) and (r.breach20 < 0.5)):
        return "broken"
    # 1) structural broken
    if (not stack) or (r.Close < r.e20) or (r.nh < 93) or (r.disp < 0.5 * disp_thr):
        return "broken"
    lifted = r.ext >= IMM_EXT
    extfam = (r.d20 >= AMBIG_D20) or (r.jump10 >= JUMP and r.d20 >= 10)
    resting = r.range5 <= FLAT_RANGE
    gentle = (-12 <= r.dd20_5 < 0)
    cons = r.ov >= OVL_HI
    # 2) extended-and-lifted family: immature / parabolic / watch
    if extfam and lifted:
        if resting and gentle and (r.d20 < 22):
            return "immature"
        if (r.d20 >= D20_HI) and (not resting):
            return "parabolic"
        return "watch"
    # 3) breakout from a base (thrust day is a large low-overlap candle -> no overlap gate)
    if (r.d20 < 10) and (r.Close > r.prior20high) and (r.chg1 > 6):
        return "breakout"
    # 4) matured / not-extended: overlap decides whether it is a real consolidation
    if not cons:
        if r.d20 >= D20_HI:
            return "parabolic"
        return "broken"  # wide / choppy non-overlapping horizontal = not a setup
    # 4a) channel has an upper distance cap: past d20=10 it already ran past the channel
    if r.d20 > 10 and (r.ext >= IMM_EXT or r.d20 >= AMBIG_D20):
        if (r.d20 >= D20_HI) and (not resting):
            return "parabolic"
        return "watch"
    if stack and resting:
        return "flag"
    if stack and (r.d20 <= 10) and ((r.stair >= STAIR_HI) or (r.micro5 >= 150)) and (r.ext >= 0):
        return "channel"
    return "flag"


def label(df):
    """Return the frame with 'state' column added (one of the 7 states or None)."""
    d = compute_features(df)
    thr = _disp_threshold(d)
    d["state"] = [_classify_row(d.iloc[i], thr) for i in range(len(d))]
    return d


def latest_state(df):
    """Convenience: (state, feature_row) for the most recent bar."""
    d = label(df)
    r = d.iloc[-1]
    return r["state"], r
