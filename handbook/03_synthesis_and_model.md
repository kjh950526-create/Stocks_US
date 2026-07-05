# Handbook 03 — Synthesis, the Actionable Model, and Scanner-vs-Prior Comparison

This merges `01` (synchronization thesis) and `02` (channel study) into what to
actually do, and answers Jeonghun's question: *does the scanner's leader criterion
agree with the older strong/weak-hand criterion?*

## 1. What the whole program established
1. **Factor co-movement** — persistent (corr 0.5–0.76).
2. **co-STATE** — when the strong hand rests, weak hands rest ~2.0–2.8× baseline;
   confirmed on eye-converged labels across **both** cyber and semi. The factor is a
   single body; you can read its state from any member.
3. **co-REST timing = null** — whether the factor rests *together* at entry adds no
   forward edge; the biggest runners come when the leader breaks *away* (co-rest OFF).
4. **Leadership = the edge** — the RS leader carries the fat right tail (runners).
5. **Entry-time ambiguity is irreducible** — the 5:5 nature of the strategy, not a bug.

## 2. The leadership result (the payoff)
RS leader = rank 1 within the factor by trailing 63-day return. Forward outcomes:

| group | fwd40 mean | P(>+20%) | P(>+40%) | top-decile | max |
|---|---|---|---|---|---|
| **RS leader (rank 1)** | **+7.5 to +9.0%** | **25–27%** | **6%** | +27–29% | **+66%** |
| rank 2 (the "chaser") | +1.7 to +2.2% | 13–14% | 3–4% | +24% | +62% |
| laggard (rank 3+) | +4.5–4.7% | 7% | **0%** | +17% | +27% |

- The leader is ~**3.5× more likely** to produce a +20% runner than a laggard; the
  **+40% monster moves come almost only from the leader**; laggards cap around +27%.
- **Requiring a clean consolidation does not help** the leader — "any valid-uptrend"
  leader (+9.0%) ≥ "consolidation" leader (+7.5%). The edge is *leadership itself*, not
  the base shape. This confirms Jeonghun's instinct that the strongest hand doesn't sit
  in a clean flag, so you must not filter it out by demanding one.
- **rank 2 is the worst group** (lowest mean, worst MAE) — it's the over-extended chaser
  right behind the leader. "Strongest hand" means literally #1, not "high-ranked".
- Honest limits: ~100 per group (fine for expectancy; the +40% tail rests on ~6 events);
  2023–26 AI bull means a few leaders (NVDA/AVGO/CRWD) produced many runners — partly a
  re-statement of "momentum concentrates in the leader". Still, validated *inside*
  Jeonghun's own factor-synchronization frame.

## 3. The actionable model
> **Identify a synchronized factor → trade its RS leader (rank 1) → do NOT demand a
> clean base and do NOT wait for co-rest permission → manage risk with the playbook.**

The original "weak-hand consolidation = permission slip" idea is **inverted**: you don't
want the factor resting in unison; you want the **leader breaking away** (co-rest OFF,
positive/rising breakaway). The synchronization thesis's practical value is not a
return-boosting entry filter — it is (a) **structure** (know which names are one body),
(b) **risk awareness** (if the whole factor is resting together, it is all exposed to
the same overnight gap — no diversification), and (c) **leader selection** (the scanner).

Execution stays with `trading_playbook_v2.md`: regime filter (🟢 only for concentration),
EMA-support or breakout trigger, **partial-profit as the primary gap defense** (no hard
stops), 3-layer sizing (per-name ≤20% cost basis; factor cap on market value incl.
runners; weak hand ≤ half of strong hand).

## 4. Scanner criterion vs the PRIOR strong/weak-hand criterion — are they consistent?
**Prior criterion (implicit, by eye):** the "strong hand" was the factor's leader chosen
by *relative strength + EMA-surf chart quality + being the archetype* (CRWD, ALAB were
treated as the strong hands); weak hands were the laggards, sized at ≤ half the strong
hand. It bundled two things — *leadership* and *chart cleanliness* — into one eye call,
and tended to *fix* a name as "the strong hand".

**Scanner criterion (mechanical):** strong = **RS rank 1 by trailing 63d return**, plus
a **breakaway** measure (how far it leads the factor equal-weight, 5d & 20d avg), plus an
independent **state** label. Leadership and chart-state are kept separate.

**Do they agree?** In spirit **yes** — both center on the relative-strength leader, so on
most days the scanner's rank-1 is the name the prior eye method would have called the
strong hand. But there are two deliberate **improvements** where they diverge, and the
divergences are *corrections*, not conflicts:
1. **Dynamic vs fixed.** The prior method mentally fixed CRWD as "strong"; the data shows
   leadership rotates (ZS→CRWD→PANW/FTNT). The scanner re-ranks daily, so it *disagrees
   with the old fixed label exactly when the old label was stale* (e.g., it would have
   flagged PANW/FTNT as cyber leaders in 2026, not CRWD).
2. **Leadership separated from base-cleanliness.** The leadership forward test proved that
   demanding a clean consolidation *dilutes* the leader's edge. So the scanner does NOT
   fold chart-cleanliness into "strong"; it reports RS-rank and state separately and lets
   you buy the leader even when it's channeling/parabolic rather than flagging. The prior
   method, by requiring a clean EMA-surf base, would have *rejected* some of the best
   leaders — a bias the scanner removes.

**So:** consistent where the old method was right (leader = RS leader), and it corrects the
old method's two biases (fixing a strong hand; over-requiring a clean base). If you ever
want to *quantify* the agreement, run the scanner historically and compare its rank-1 to
whichever name you had been calling "the strong hand" on the same dates — expect high
overlap except during leadership-rotation transitions, which is exactly where the scanner
is more correct.

## 5. How to keep using this
- New session → `README.md` → `STATUS.md` → handbooks → run `engine/scanner.py`.
- The scanner narrows *where to look*; you decide entries/sizing via the playbook.
- Calibration can resume (diminishing returns) to shave the ambiguous zone or fix the
  prior-trend-gate residual (add a "recent real thrust" feature). See `02` §3.
- Expand `WATCHLIST` in `scanner.py` beyond cyber/semi as the book grows.
