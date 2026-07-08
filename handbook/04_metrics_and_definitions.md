# Handbook 04 — Metrics & Definitions (강손/약손 방법론 레퍼런스)

**Purpose:** a self-contained glossary so any new session (or Jeonghun) can immediately
understand *exactly* how every term is computed and *why* the strong-hand / weak-hand
(강손/약손) designation is done the way it is. Written after a session where Jeonghun
asked for the precise definitions and how they map to his own mental model. Read this
whenever "동조성 / 결합도 / 리더십 / RS / breakaway / ADR" appear.

---

## 1. The building block — daily return (일봉 리턴)
`r_t = Close_t / Close_{t-1} − 1`  (for correlation math use the log return
`ln(Close_t / Close_{t-1})`). Everything below is built from this.

## 2. Correlation = 동조성 (co-movement)
Pearson correlation of two names' daily (log) returns over a window (we use 60d, and 42d
for the ~2-month view):
`corr(A,B) = cov(r_A, r_B) / (σ_A · σ_B)`, range −1…+1.
- **What it measures:** whether they move in the SAME DIRECTION on the same days.
- **Critical property:** it divides by each name's own volatility (σ), so it is
  **already volatility-/ADR-normalized**. corr = 0.6 means "same direction most days",
  it does NOT mean "same size move". Two names can be 74% same-direction yet have a
  lower correlation if their magnitudes differ a lot (that is exactly the semi case:
  ALAB moves far more than AVGO, so high sign-agreement but only ~0.48 correlation).

## 3. Same-direction % (동일방향일 %)
Fraction of days where `sign(r_A) == sign(r_B)`. This is the literal "+와+, −와−" metric
(both up or both down on the same day). Typical strong↔weak pairs run ~69–74%. It is the
sign-only companion to correlation (which also weights magnitude).

## 4. Average coupling = 전체 평균 결합도
The average of ALL pairwise correlations among a factor's members (e.g. cyber has 4
names → 6 pairs → average their correlations). Answers "how much is the whole factor one
body?".
- Snapshot (60d, as of 2026-07-07): **cyber +0.68** (tightest) · fintech +0.53 ·
  **semi +0.52** · **defense +0.27** (loosest).
- Note: semi's *normal* coupling (~0.52) is similar to fintech; a synchronized CRASH
  temporarily pumps its members' correlation toward 1 (everything dumps together), which
  can make semi *look* far more coupled than it is in calm periods. Do not mistake a
  crash-inflated correlation for structural tightness.
- Practical use: the strong/weak co-movement read (약손 쉬면 팩터 pause) is reliable on
  a tightly-coupled factor (cyber) and NOISY on a loose one (defense 0.27, where the
  leader AXON is almost a lone actor — corr to RTX/LMT ~0.1). On loose factors lean more
  on the leader's own chart than on the weak-hand comparison.

## 5. Relative Strength (RS) — how the LEADER (강손) is chosen
`RS = trailing 63-day return (%)`. Rank factor members by RS descending; **rank 1 = the
leader = 강손.** The weak hand (약손) is a low-RS laggard that still co-moves (decent
correlation), used only as a "is the factor resting?" gauge and sized ≤ ½ the strong hand.
- **RS uses RAW cumulative return — deliberately NOT ADR-normalized** (see §8).

## 6. Leadership — the research finding (not a per-day metric)
From the forward-return test (handbook 03): within a synchronized factor the RS leader
(rank 1) captures the **fat right tail** — P(forward-40d > +20%) ≈ 25–27% for the leader
vs ≈ 7% for a laggard; the +40% monster runs come almost only from rank 1; rank 2 (the
"chaser") is historically the WORST forward group. So "leadership" operationally = "the
RS-rank-1 name is the one that produces the monster runners." This is *why* we trade the
leader and treat the weak hand as a comparison gauge, not a return vehicle.

## 7. Breakaway (scanner metric)
Per name, the average daily EXCESS return vs the factor equal-weight, over 5d and 20d
(`breakaway = mean(r_name − r_factor_ew)`). Positive/rising breakaway = the name is
LEADING the factor (pulling away). Research note: the biggest runners come when the
leader breaks AWAY from the factor (co-rest OFF), so breakaway is a signal, not "permission".

---

## 8. The key reconciliation — RS vs Jeonghun's per-day mental model
Jeonghun's intuition for defining strong/weak: within a factor, on UP days the strong
hand rises MORE, on DOWN days the weak hand falls MORE, with direction shared (both + or
both −), and this magnitude should be **ADR-normalized** (not absolute). His question:
isn't that how strong/weak are picked?

**Answer — his model is correct and RS is its cumulative form.** "Strong goes up a bit
more and falls a bit less, every day" *accumulates* into a higher 63-day return = a
higher RS rank. So RS-rank is the integrated (63-day) version of his per-day "who is
stronger" battle. Same idea, different time-scale; RS is used because one 63-day number
is far less noisy than judging sign+magnitude day by day, and because RS-rank is what was
directly validated against forward returns.

**The data confirms his model literally** (2-month window, strong↔weak pairs): same-
direction ≈ 69–74% (direction shared) BUT cumulative return strong +45…+83% vs weak
−13…+11% (strong pulls away in MAGNITUDE). That divergence in magnitude *is* leadership.
Also note the strong↔weak pair correlation (0.48–0.57) is LOWER than the factor's average
coupling (e.g. cyber 0.68) — expected, because the leader and the worst laggard are by
construction the two most divergent members of the factor.

## 9. ADR-normalization — where it applies and where it does NOT
Jeonghun is right that comparing "who moves more" fairly requires normalizing by each
name's own volatility (ADR/σ), else a high-ADR name looks "strong" just from being jumpy.
- **Correlation already normalizes** (divides by σ), so the 동조성/결합도 metrics are
  volatility-fair.
- **RS (raw 63d return) is deliberately NOT ADR-normalized.** The strategy's edge is the
  fat right tail, which lives in names making big RAW moves. ADR-normalizing RS would
  penalize exactly the high-ADR names (ALAB ADR ~10.5, DAVE ~8.5) that PRODUCE the
  monster runs. So for LEADER SELECTION we want the raw-return leader (high ADR welcome).
- **ADR comes back for SIZING, not selection:** the risk-based size formula
  `size = (capital × risk%) / SL%` absorbs ADR there (a high-ADR name has a wider SL% →
  smaller notional). Rule of thumb also: judge STOP WIDTH as an ADR multiple (~1.5–2.5×
  ADR), not an absolute %; a 15% stop on ADR-8.5 DAVE is 1.8× ADR (fine), the same 15% on
  ADR-2.5 RTX is 6× ADR (absurd). See playbook §4.
- One-liner: **ADR-normalize for sizing; raw return for leader selection.**

## 10. Current strong/weak pairs & pair correlations (snapshot 2026-07-07)
Ranked by daily-return agreement strength (2-month window):
| factor | strong (강손) | weak (약손) | pair daily-corr | same-dir% | strong 2mo | weak 2mo |
|---|---|---|---|---|---|---|
| fintech | DAVE | SOFI | 0.57 | 71% | +45.5% | +10.8% |
| defense | AXON | PLTR | 0.53 | 71% | +68.3% | −1.1% |
| cyber | PANW | ZS | 0.52 | 69% | +83.2% | +5.8% |
| semi | ALAB | AVGO | 0.48 | 74% | +77.5% | −13.2% |
(Weak hands confirmed by RS-rank + co-movement: cyber ZS, fintech SOFI, defense PLTR;
semi AVGO chosen as a co-moving laggard. AFRM is a *second strong hand*, not a weak hand.
For defense, RTX/LMT are near-uncorrelated to AXON (~0.1) so they are poor comparison
weak hands — AXON is nearly a lone actor there.)

## 11. How this is produced (tooling)
`engine/scanner.py` emits, per factor: RS rank, trailing 63d return, breakaway (5d/20d),
state, ADR%, %-of-60d-high. Correlations/coupling are ad-hoc computed from Yahoo EOD
daily log returns (60d or 42d windows). Data source = Yahoo EOD (split-adjusted); see
`README.md` data policy.
