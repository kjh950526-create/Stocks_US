# Handbook 02 — The Channel Study (eye-calibration → converged label engine)

## 1. The reframe that started it
Standard Qullamaggie hunts a clean flag then a breakout. But the **strongest hand does
not rest in a clean flag** — its relative strength is so high that even its "rest" gets
pushed upward into a **rising channel** (a *displaced consolidation*). So a flag-only
filter *automatically drops the strongest hand* and only catches visibly-resting 2nd-tier
names. To catch the strongest hand you must buy the channel — which, seen alone, looks
like adding strength to strength (reckless).

The original hypothesis to rescue that: the synchronized factor lets you read the
factor's "rest" from the **weak hands** (which *do* visibly consolidate). Weak-hand
consolidation = the factor is pausing = **permission** to buy the strong hand's channel,
reinterpreting a scary channel as a "displaced consolidation". → This is what the study
set out to test, and it required teaching the code to *see* these states like Jeonghun.

## 2. Why a 7-round human-in-the-loop calibration
To test any of this we needed labels ("is the strong hand in a channel / immature base /
just parabolic?") that match Jeonghun's trained eye. A self-contained HTML **quiz tool**
was built: it shows real 60-day candlestick charts (CRWD/PANW/FTNT/ZS + ALAB/NVDA/AVGO/
AMD/MRVL) with EMA10/20/50, asks Jeonghun to classify the last (decision) bar, then
reveals the mechanical label + numeric readouts, and logs every disagreement (plus a
free-text one-line reason per item from round v4 on). Each round's disagreement JSON was
fed back to re-derive thresholds. **Agreement rate is not the metric** — the metric is
whether each round surfaced a *new systematic axis* the eye uses.

## 3. What each round discovered (the eye's feature axes)
| Round | Discovery |
|---|---|
| v1–v2 | Parabolic vs channel is judged by **acceleration** (5d slope vs 20d slope, "curving up") and by distance from EMA**20** (d20), not distance from EMA10. |
| v3 | Overcorrected: dropped the distance axis for pure acceleration — broke. Lesson: eye uses **both** distance and acceleration. |
| v4 | **Immature is a SEQUENCE, not a snapshot:** prior vertical jump → *then* sideways → *while* the EMA catches up (Δd20 < 0). Cannot be判정 on the jump day itself. |
| v5 | **Prior-trend gate** is the single biggest missing axis: a valid setup REQUIRES a pre-existing uptrend ("우상향 context"). Without it, any shape = broken. |
| v6 | **OVERLAP is the physical definition of "consolidation":** candles' [low,high] must overlap. No overlap = vertical extension (parabolic) or wide chop (= broken). Channel = overlap + **HH & HL stair** stepping up (or riding the EMA). Prior-trend gate raised to **EMA20** (a strong hand rides the 10/20 line; going to the 50 = disqualified). |
| v7 | **Convergence:** no new axis. Only two threshold tweaks remained (prior-trend ≥75% above EMA20 with no recent 3% breach; channel capped at d20 ≤ 10). Remaining disagreements are (a) one residual gate imperfection and (b) an **irreducible ambiguous zone** the trader himself labels "observe / could go either way". |

## 4. The converged 7-state definition (see `engine/strong_hand_engine.py`)
- **broken** — prior-trend gate fails (needs ≥75% of prior-50d closes above EMA20, EMA20
  rising, no close ≤ EMA20−3% in last 20d); or stack broken / close < EMA20 / off highs
  (nh<93) / EMAs collapsed (disp < ½ own-threshold); or a wide non-overlapping horizontal.
- **flag** — overlapping candles, sideways near the EMAs (range5 ≤ 8%).
- **channel** — overlapping candles stepping up (HH&HL stair ≥ 35% of last 6, or driving)
  while displaced but not far (ext ≥ 0, d20 ≤ 10).
- **parabolic** — very extended (d20 ≥ 18) and still surging (not sideways / no overlap).
- **breakout** — from a base (d20 < 10), new 20d high + a >+6% thrust day.
- **immature** — jumped (max d20 in last 10d ≥ 18), now sideways (range5 ≤ 8%), EMA
  catching up gently (−12 ≤ Δd20 < 0), still lifted off EMA10 (ext ≥ 7), d20 < 22.
- **watch** ("미성숙후보 / observe") — extended + jumped but consolidation not yet formed
  (still widening or not sideways). The honest "cannot tell yet" bucket.

Key numeric readouts the eye maps to: overlap% (consolidation), stair% (HH&HL), d20
(extension vs EMA20), ext (distance off EMA10 / "lifted"), Δd20 (EMA catch-up), jump10
(recent vertical move), prior_above20% (uptrend context), range5 (sideways tightness).

## 5. Re-tests on the converged labels
1. **co-state lift (re-confirmed, both factors):** per-anchor lift
   CRWD 2.45 · PANW 2.45 · FTNT 1.56 · ZS 2.82 · NVDA 2.33 · AVGO 2.68 · AMD 2.14 ·
   MRVL 2.42. All ≥1.5, and it **replicates on semiconductors** — strong external
   validation of the mechanism.
2. **co-rest forward test (null, replicated on trusted labels):** consolidation entries
   split by co-rest (≥2 weak members also resting). ON (n=48) vs OFF (n=241):
   ON fwd40 +5.6% / OFF +4.8%, but **ON has a WEAKER right tail** — P(fwd40>+20%) 8% vs
   17%, max +37% vs +66%. The biggest runners come when the strong hand rests ALONE
   (OFF). Calibrating labels did not rescue a co-rest edge that isn't there. (One hint:
   ON's extreme MAE 5th-pct was less bad, −18% vs −26% — a possible *risk* angle, not a
   return angle; small N.)
3. **Leadership forward test (confirmed) — see `03`:** the real edge is RS leadership.

## 6. Caveats to remember
- Entries in the forward tests are ~95% **flag** (channel/immature are rare in population
  and were de-overlapped to episode-starts) — so co-rest was effectively tested on flags.
- Mechanical N-day-hold forward returns ≠ Jeonghun's actual execution (partial profits +
  runner trailing). The strategy's P&L lives in runner management, which a fixed hold
  cannot capture.
- Tail claims are inherently low-power at these sample sizes; treat as directional.
