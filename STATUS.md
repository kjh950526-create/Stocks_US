# STATUS — read first to resume

_Last updated: 2026-07 (channel study completed, scanner shipped)._

## Where the research stands (conclusions)
| Claim | Verdict | Evidence |
|---|---|---|
| Same factor moves together (persistent co-movement) | **Confirmed** | Rolling 20/60d return correlation 0.5–0.76, 2020–2026 |
| Strong hand rests → weak hands rest (co-STATE) | **Confirmed** | co-state lift ~2.0–2.8 on eye-converged labels, **both** cyber & semi cohorts |
| co-REST (factor resting together) is a forward/timing edge | **Null** | ON vs OFF: no better returns, ON has *fewer* big runners; tail power low |
| **RS leader (rank 1) carries the fat right tail (runners)** | **Softened (2012–2026 re-test)** | Leader edge REAL but MODEST: rank1 6.5% vs laggard 4.7% (~1.8pp), NOT +7.5–9%. "rank2 worst" REJECTED (≈laggard). "monsters only from leader" FALSE (single biggest +182% was a laggard). Prior figures were an AI-boom small-sample artifact. See handbook 05 |
| **Leader edge is FACTOR-DEPENDENT** | **New (2012–2026)** | leader−laggard: solar +5.0 / semi +4.4 / megatech +1.7 / cyber +1.3 / software −2.3. Big in high-dispersion/high-beta factors, negative in software → factor choice matters as much as stock choice |
| Leadership persists; within-factor correlation rises in bear | **New** | P(leader stays) 58–74%, tenure 24–38 trading days; factor corr 0.46–0.56 overall → 0.55–0.68 in bear (gap risk peaks exactly when correlation peaks) |
| Requiring a clean consolidation helps the leader | **No** | "any valid-uptrend" leader (+9.0%) ≥ "consolidation" leader (+7.5%); the base filter dilutes |
| Entry-time state (immature/watch/channel) is cleanly decidable | **No (irreducible)** | Jeonghun himself labels these "observe/ambiguous"; = the 5:5 nature of the strategy |

**Actionable model:** synchronized factor → trade its **RS leader** → do not require a
clean base, do not wait for co-rest → risk via playbook (partials + 3-layer sizing, no
hard stops). See `handbook/03_synthesis_and_model.md`.

### Open research tasks (2026-07-15, 검증 후 채택 결정 — 지금 실전 변경 없음)
1. **되돌림 국면 2R 풀익절 vs 트레일 런** — ✅ 백테스트 완료(2011-26, 2785건, 리더 진입,
   1R=2ADR, 레짐분할). 결과: **트레일 런이 전 국면서 근소 우위** (bull +0.29%p, bear +0.40%p,
   전체 +0.37%p). 승률 동일(44%), 차이는 순전히 우측꼬리(트레일 max +81% vs 풀익절 +66%).
   **"톱질/약세장엔 풀익절 유리" 가설 기각** — 러너 우측꼬리가 약세장에도 살아있음. ⚠️ 단
   백테스트에 **갭·무하드스탑·종가1회 미반영**(트레일에 유리하게 편향) + bear 표본 바닥반등
   selection 편향. 실전 결론: **러너 트레일 유지(§5), 풀익절 전환 근거 약함. 톱질장 대응은 출구
   변경이 아니라 입구 축소(현금).**
2. **하락장 인버스ETF/지수풋 방어** — 개별주 숏은 여전히 실전 NO(§7-1: 갭업 무한). 인버스ETF/
   지수풋으로 하락장 방어가 백테스트상 되나? **연구/페이퍼 트랙만, 실전 아님.** 롱 검증 완료 +
   stage-2 이후에나 실전 검토.

### 리더엣지 시변성 (2026-07-15, handbook 05 정교화)
- 팩터별 리더엣지는 **고정 상수 아님 — 시계열로 출렁**(solar σ9 범위 −8~+25, semi −5~+14).
- **같은 팩터도 부호 뒤바뀜**(semi 2018~20 음수 → 2023~26 강양수). 시장 전체적으로 "리더엣지
  강한 시기(추세장: 2015·2019·2023~25) vs 약한 시기(톱질장: 2012·2016)"가 있음.
- ★방법론 한계(Jeonghun 지적): RS는 후행 → 로테이션 국면엔 "과거 리더 ≠ 미래 리더". "리더엣지
  음수" = 약손이 강손을 이긴 게 아니라 **모멘텀 지속(추세) vs 되돌림(톱질) 국면의 함수**. 팩터
  변동성이 그 경향 조절(고베타=지속 잦음, 저베타=되돌림 잦음).
- **함의: 리더 사는 건 "모멘텀 지속" 베팅 = 추세장 전용.** 내 전략 자체가 추세장 사양(결함
  아님). 톱질/하락장 정답 = 스타일 변경이 아니라 **현금**(안 싸움). 하락장 롱은 압도적 리더
  명백할 때만 소액. 스타일 다변화(숏·풀익절)는 stage-2 페이퍼검증 후.

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
   - **2026-07 snapshot (Yahoo EOD 07-02):** clear **semi → cyber rotation** — cyber
     +15% 5d, all leaders at nh 98–99; semi factor-wide `broken`, 10–25% off highs
     (SOX −6.7% on 07-01, distribution after good earnings). **fintech** added as the
     strongest alt-factor (20d +27%, AI-capex-uncorrelated), **defense** added (+9% 20d,
     rotation beneficiary). power/nuclear/quantum/space all 🔴 (correcting/broken).
   - **DAVE / AXON / HOOD = TRACK ONLY** (just broke a downtrend into V-shaped new highs;
     wait for a first consolidation before treating as actionable). See playbook §11.
   - Positions: **CRDO closed at breakeven**; **CRWD 4:1 split 07-02** (entry $703.39 →
     $175.85 adjusted, ~$194 now, +10%). **ALAB runner CLOSED 2026-07-06 @ $402.19
     (+3.1%; first live §4-1 BE-defense front-run); CRDO closed ~BE.** Only position now
     = CRWD (cyber 🟢). Semi slice fully defended out; no new setups → cash + wait.
5. **Calibration can resume** any time: `handbook/02_channel_study.md` documents the
   loop and the calibration HTML tool design. More rounds mainly shave the residual
   ambiguous zone (diminishing returns).

## How live trading connects
The scanner narrows *where to look*; the human `trading_playbook_v2.md` decides regime
(🟢/🟡/🔴), entry trigger (EMA-support or breakout), partial-profit defense, and 3-layer
sizing (per-name ≤20% cost basis, factor cap on market value, weak hand ≤ half of strong).
