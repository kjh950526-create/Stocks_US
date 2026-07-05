# STATUS — read first to resume

_Last updated: 2026-07 (channel study completed, scanner shipped)._

## Where the research stands (conclusions)
| Claim | Verdict | Evidence |
|---|---|---|
| Same factor moves together (persistent co-movement) | **Confirmed** | Rolling 20/60d return correlation 0.5–0.76, 2020–2026 |
| Strong hand rests → weak hands rest (co-STATE) | **Confirmed** | co-state lift ~2.0–2.8 on eye-converged labels, **both** cyber & semi cohorts |
| co-REST (factor resting together) is a forward/timing edge | **Null** | ON vs OFF: no better returns, ON has *fewer* big runners; tail power low |
| **RS leader (rank 1) carries the fat right tail (runners)** | **Confirmed** | P(fwd40>+20%): leader ~25–27% vs laggard ~7%; +40% moves almost only from leader; max +66% vs +27% |
| Requiring a clean consolidation helps the leader | **No** | "any valid-uptrend" leader (+9.0%) ≥ "consolidation" leader (+7.5%); the base filter dilutes |
| Entry-time state (immature/watch/channel) is cleanly decidable | **No (irreducible)** | Jeonghun himself labels these "observe/ambiguous"; = the 5:5 nature of the strategy |

**Actionable model:** synchronized factor → trade its **RS leader** → do not require a
clean base, do not wait for co-rest → risk via playbook (partials + 3-layer sizing, no
hard stops). See `handbook/03_synthesis_and_model.md`.

## The tooling
- `engine/strong_hand_engine.py` — converged **v7** 7-state classifier (broken / flag /
  channel / parabolic / breakout / immature / watch). Product of a 7-round human-eye
  calibration; thresholds are provisional but eye-anchored.
- `engine/scanner.py` — run `python3 scanner.py`. Prints, per factor: RS rank, trailing
  63d return, **breakaway** (5d & 20d avg lead vs factor equal-weight), state, %-of-60d-high.
  Flags the leader. Edit `WATCHLIST` to add factors/names.

## Known issues / environment
- **IBKR MCP connector: BROKEN.** The harness stringifies integer/boolean params, so
  `get_price_history` / `get_price_snapshot` fail schema validation. String-only tools
  (`search_contracts`, `get_theme_details`, `search_investment_topics`) still work.
  This is a platform-level bug, not fixable from a session. **Workaround: use Yahoo EOD
  for all prices.** Revisit if/when Anthropic fixes it.
- **stooq.com: permanently blocked** from datacenter IPs (TCP timeout, not an allowlist
  issue; "All domains" does not help). Yahoo is the permanent price source.
- Data source is intentionally invisible to the user; just use Yahoo EOD, minimise usage.

## Open items / next candidates
1. **Formalise the leader signal** further: RS-rank-1 + positive/ rising breakaway +
   state != broken. (Scanner already emits these; could add a single composite score.)
2. **Left-tail / gap defense re-test** (deferred): the one place co-rest ON looked
   better was the extreme MAE 5th-percentile. Worth a larger-N check as a *risk* filter
   (not a return booster), given the no-hard-stop environment.
3. **Prior-trend gate residual**: still lets through some "weak uptrend context" cases;
   the clean separator is likely "was there a real recent momentum thrust" — an extra
   feature to add if calibration continues.
4. **Watchlist expansion** beyond AI-capex (cyber/semi). Prior scans rejected HWM, GE,
   AEM, BSX, HIMS; SPHR removed (debt-restructuring). FIX/AGX flagged fractional-price
   ineligible on Toss. Add factors as the book grows and re-run the scanner.
5. **Calibration can resume** any time: `handbook/02_channel_study.md` documents the
   loop and the calibration HTML tool design. More rounds mainly shave the residual
   ambiguous zone (diminishing returns).

## How live trading connects
The scanner narrows *where to look*; the human `trading_playbook_v2.md` decides regime
(🟢/🟡/🔴), entry trigger (EMA-support or breakout), partial-profit defense, and 3-layer
sizing (per-name ≤20% cost basis, factor cap on market value, weak hand ≤ half of strong).
