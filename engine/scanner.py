"""
scanner.py
==========
Daily "strongest-hand" scanner for synchronized factors.

Empirical basis (see handbook/03_synthesis_and_model.md):
  * The factor moves/rests together (co-state lift ~2.0-2.8, both cyber & semi).
  * Within a synchronized factor, the RS LEADER (rank 1 by trailing 63d return)
    captures the fat right tail: P(fwd40 > +20%) ~25-27% for the leader vs ~7%
    for laggards; the +40% monster runners come almost ONLY from the leader.
  * Requiring a clean consolidation does NOT help the leader (it slightly dilutes)
    -> do not filter the leader on "clean base"; the edge is leadership itself.
  * co-rest (whole factor resting together at entry) does NOT add forward edge;
    if anything the biggest runners come when the leader breaks AWAY from the
    factor (co-rest OFF). So "breakaway" is a signal, not "permission".

What the scanner does per run:
  For each factor, fetch EOD data, label each name's strong-hand STATE, rank
  members by relative strength (trailing 63d return), and measure BREAKAWAY
  (how far the name leads the factor's equal-weight, today / 5d avg / 20d avg).

  Output columns per name:
    rs_rank      1 = leader (buy candidate), 2 = chaser (historically WORST - avoid),
                 3+ = laggard
    rs_63d       trailing 63-day return (%)
    breakaway_5d avg daily excess-vs-factor over last 5 days (%/day)  <- "recent lead"
    breakaway_20d avg daily excess-vs-factor over last 20 days (%/day)
    state        converged strong-hand state (broken/flag/channel/parabolic/
                 breakout/immature/watch)
    nh           % of 60d high

  The scanner NARROWS where to look (rs_rank==1, positive breakaway, state != broken).
  Final entry / sizing / runner management stays with the human playbook
  (trading_playbook_v2.md): regime filter, EMA-support or breakout trigger,
  partial-profit defense, 3-layer sizing.

Usage:
    python scanner.py                 # scans the default WATCHLIST, prints table
    python scanner.py --csv out.csv   # also writes a CSV

Edit WATCHLIST below to track your own factors/names. The engine only "knows"
whatever you give it; expand beyond AI-capex names as your book grows.
"""

import argparse
import numpy as np
import pandas as pd

import strong_hand_engine as E

# --------- EDIT ME: factors -> tickers you want to track ---------
WATCHLIST = {
    "cyber":   ["CRWD", "PANW", "FTNT", "ZS", "S", "OKTA"],
    "semi":    ["ALAB", "NVDA", "AVGO", "AMD", "MRVL"],
    "fintech": ["DAVE", "AFRM", "SOFI", "NU"],   # added 2026-07: strongest factor (20d +27%)
    "defense": ["AXON", "RTX", "PLTR", "LMT"],   # added 2026-07: "Great Rotation" beneficiary
    # NOTE: DAVE/AXON/HOOD just broke a downtrend into V-shaped new highs -> TRACK ONLY
    # until a first consolidation forms (engine tags them 'broken' via the prior-trend gate).
    # add your own, e.g. "power": ["GEV","VRT",...], "nuclear":[...]
}
RS_LOOKBACK = 63     # trailing days for relative-strength ranking (~3 months)


def _excess_series(closes, factor_ew):
    """daily return of a name minus the factor equal-weight daily return."""
    ret = closes.pct_change()
    return (ret - factor_ew)


def scan(watchlist=WATCHLIST):
    rows = []
    for factor, tickers in watchlist.items():
        labeled = {}
        closes = {}
        for t in tickers:
            try:
                df = E.fetch_yahoo(t)
                labeled[t] = E.label(df)
                closes[t] = labeled[t]["Close"]
            except Exception as ex:
                print(f"  [warn] {t}: fetch/label failed ({ex})")
        if not closes:
            continue
        px = pd.DataFrame(closes).dropna(how="all")
        factor_ew_ret = px.pct_change().mean(axis=1)          # equal-weight factor return
        rs63 = (px / px.shift(RS_LOOKBACK) - 1) * 100          # trailing 63d return %
        rs_rank = rs63.rank(axis=1, ascending=False, method="min")
        for t in closes:
            excess = _excess_series(px[t], factor_ew_ret)      # daily excess vs factor
            last = labeled[t].iloc[-1]
            rows.append({
                "factor": factor,
                "ticker": t,
                "rs_rank": int(rs_rank[t].iloc[-1]) if not np.isnan(rs_rank[t].iloc[-1]) else None,
                "rs_63d": round(float(rs63[t].iloc[-1]), 1) if not np.isnan(rs63[t].iloc[-1]) else None,
                "breakaway_5d": round(float(excess.tail(5).mean()) * 100, 2),
                "breakaway_20d": round(float(excess.tail(20).mean()) * 100, 2),
                "state": last["state"],
                "adr20": round(float(last["adr20"]), 2) if not pd.isna(last["adr20"]) else None,
                "nh": round(float(last["nh"]), 1) if not pd.isna(last["nh"]) else None,
                "d20": round(float(last["d20"]), 1) if not pd.isna(last["d20"]) else None,
                "asof": labeled[t].index[-1].date().isoformat(),
            })
    out = pd.DataFrame(rows)
    if len(out):
        out = out.sort_values(["factor", "rs_rank"], na_position="last").reset_index(drop=True)
    return out


def format_table(df):
    if not len(df):
        return "(no data)"
    lines = []
    for factor, g in df.groupby("factor"):
        lines.append(f"\n=== {factor.upper()} ===  (as of {g['asof'].iloc[0]})")
        lines.append(f"{'name':<6}{'RS#':>4}{'rs63d':>8}{'brk5d':>8}{'brk20d':>8}  {'state':<10}{'ADR%':>6}{'nh':>6}")
        for _, r in g.iterrows():
            lead = " <- LEADER" if r["rs_rank"] == 1 and r["state"] not in (None, "broken") else ""
            lines.append(f"{r['ticker']:<6}{str(r['rs_rank']):>4}{r['rs_63d']:>8}"
                         f"{r['breakaway_5d']:>8}{r['breakaway_20d']:>8}  "
                         f"{str(r['state']):<10}{str(r['adr20']):>6}{r['nh']:>6}{lead}")
    lines.append("\nleader = rs_rank 1 AND state != broken (buy candidate; confirm on chart).")
    lines.append("avoid  = rs_rank 2 (historically the worst forward group - the chaser).")
    lines.append("ADR% = proper high/low range. STRONG hand needs high ADR (~>4) + verified")
    lines.append("fundamentals; the WEAK/comparison hand may be low-ADR & is fundamentals-exempt.")
    return "\n".join(lines)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=None, help="write results to this CSV path")
    args = ap.parse_args()
    df = scan()
    print(format_table(df))
    if args.csv:
        df.to_csv(args.csv, index=False)
        print(f"\nwrote {args.csv}")
