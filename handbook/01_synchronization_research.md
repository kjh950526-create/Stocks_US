# Handbook 01 — The Synchronization Thesis (research BEFORE the channel study)

This documents the quantitative research track as it stood before the 7-round
channel/eye-calibration study (that study is `02_channel_study.md`). Together they
form one continuous program; read them in order.

## 1. The thesis (as re-defined)
> **Members of the same factor synchronize and move together regardless of direction.**
> So when the strong hand pulls back / rests inside its EMA channel, *at that same
> moment* the weak hands are in the same state — the whole factor is catching its
> breath. Buying then = buying the factor's pause. **Direction (surge vs collapse) is
> secondary; simultaneity is the substance.**

Judgement is by co-movement, not by A/B/C direction. High strong↔weak correlation
during the strong hand's consolidation = support; low/negative = decoupling (refutation).
Lead-lag is explicitly NOT claimed (lag0 only). Cases where strong and weak both fall
together still *support* the thesis (it is about co-movement, not upside).

## 2. Locked analysis options (pre-registered, do not silently change)
1. Rolling correlation at **both 20d and 60d**.
2. Threshold **0.55** as a label (not a hard cut).
3. **lag0 only** (no lead-lag).
4. State judged on **MA20 / EMA20**.
5. Slope band **±20% annualized**, same yardstick for strong & weak, relative comparison.
6. Low volatility = **bottom 33%** of a name's own history.
7. Volatility = **std of log returns**.
8. Correlation on **log returns**.
9. Hybrid labeling: code filters the obvious, human eyes the ambiguous.
10. Data = **Yahoo EOD split-adjusted** (stooq is IP-blocked; permanent).
11. Daily bars, wide window, exclude the first ~1yr post-listing (unstable).

## 3. Empirical pipeline (built + validated on synthetic, then real)
Data ingestion (Yahoo) → log returns → rolling 20/60d Pearson correlation →
co-state concordance test → forward-return analysis. The engine was validated on
synthetic data (one strong hand + one synchronized weak hand + one decoupled weak
hand were separated cleanly by correlation) before running on real names.

## 4. Cohorts tested (2020–2026)
- **Cybersecurity:** CRWD, PANW, FTNT, ZS (+ S, OKTA as robustness).
- **Semiconductors:** ALAB, NVDA, AVGO, AMD, MRVL.
- ALAB IPO'd 2024-03 (short history); S IPO'd 2021-06.

## 5. Key empirical findings (prior track)
- **Baseline synchronization confirmed:** rolling correlations 0.5–0.76 across the
  window. Tightest cyber pair CRWD–PANW (~0.62–0.64); loosest CRWD–FTNT (~0.51–0.56).
  There is a *coupling hierarchy* inside a factor.
- **Decoupling control — the July 2024 CrowdStrike outage.** CRWD's idiosyncratic
  global-outage crash (−11% on 2024-07-19, then −13% more, sliding to ~−35%) while
  FTNT/PANW were flat-to-up. 20d rolling correlation CRWD↔peers collapsed from ~0.55
  to ~0.05 during the window and recovered afterward, while the two unaffected names
  (FTNT↔PANW) stayed coupled. → the correlation detector correctly separates
  "factor pause" from "one name's accident".
- **co-STATE concordance:** the *specific* claim ("when strong rests, weak rests") is
  a co-STATE claim, which plain return-correlation does NOT measure (correlation =
  "same direction", not "same state"). Measured properly as
  `lift = P(weak in consolidation | strong in consolidation) / P(weak in consolidation)`,
  early runs gave **lift 2.0–2.6** (all ≥ pre-registered 1.5), so the mechanism holds.
- **Forward weak-hand-permission filter = null.** No detectable forward edge from the
  "weak hand confirms" filter — as expected for a low-win-rate, fat-tailed model, and
  the tail comparison is inherently underpowered.

## 6. Leadership rotation (important context)
CRWD is **not** a stable "strong hand" — it is the highest-*amplitude* (highest-beta)
name. Leadership rotates:
- 2020–21: ZS led (+215%).
- 2023–mid 2024: CRWD dominated (+232%) — this is why it got mentally fixed as "strong".
- 2026 YTD: **PANW / FTNT led (+94% / +101%)**, CRWD lagged (+71%).
Max drawdowns (since listing): CRWD −68%, PANW −47%, FTNT −38% (steadier), ZS −76%,
S −84%, OKTA −85%. **May 2026 was a factor-wide co-surge** (CRWD +64%, PANW +57%,
FTNT +64% in one month) — the synchronization thesis on the upside.
→ Do NOT hard-code a name as "strong". Leadership is dynamic (this motivated the
RS-rank scanner in `02`/`03`).

## 7. Infra notes carried forward
- Price source: **Yahoo EOD** (stooq permanently IP-blocked from datacenter ranges;
  not an allowlist bug — a TCP-level block; "All domains" does not help).
- IBKR MCP connector broken (int/bool param serialization); use string-only IBKR tools
  only, prices from Yahoo.
- Stack: Python + pandas; self-contained HTML calibration tool with EMA10/20/50 overlays.
- Reference framework: Qullamaggie (콜라매기) momentum; see `trading_playbook_v2.md`.
