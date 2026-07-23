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
- **IBKR MCP connector: PARTIALLY WORKING (2026-07-20 재검증).** 이전 기록("전면 broken")은 부정확.
  - ❌ **가격 툴만 broken:** `get_price_history` / `get_price_snapshot` (정수 파라미터 직렬화 버그).
    → 가격은 계속 **Yahoo EOD** 사용.
  - ✅ **계좌 툴은 정상 작동** (파라미터가 없어서 버그를 안 탐): `get_account_positions`,
    `get_account_summary`, `get_account_balances`, `get_account_orders`, `get_account_trades`.
    → **연결된 계좌의 포지션·평단·잔고·주문·체결을 Claude가 직접 읽을 수 있다.** 스크린샷 불필요.
  - ✅ **`search_contracts` 정상**, 그리고 ★**주문 초안 워크플로 전 과정 검증 완료**★:
    `search_contracts`(종목→contract_id) → `create_order_instruction`(초안 생성, 실주문 아님) →
    **딥링크 URL 반환** → 사용자가 IBKR 모바일에서 검토 후 **버튼 하나로 제출**.
    `get_order_instructions`(목록) / `delete_order_instruction`(삭제)도 작동. 초안은 7일 후 만료.
    → **Claude가 미리 주문 초안을 만들어두고 사용자는 확인·제출만 하면 된다** (취침 중 대비 가능).
  - ⚠️ 초안·조회가 **어느 계좌로 가는지는 커넥터에 연결된 계좌**에 달림. 페이퍼 운용 시 반드시
    **페이퍼 계좌로 연결**되었는지 확인할 것.
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

---

## 페이퍼 라이브 포지션 (2026-07-22~)

**계좌:** IBKR 페이퍼 $20,000, 하드스탑 ON, 정수주. 커넥터 연결됨(Claude가 직접 읽음).

| 종목 | 팩터 | 진입일 | 평단 | 수량 | 하드SL | 실리스크 | 논리 |
|---|---|---|---|---|---|---|---|
| **DAVE** | 핀테크(리더) | 2026-07-22 | $425.07 | 9주 | **$409 GTC** | 0.7% | 10선 존터치($416저점) 반등=트리거A |

- 진입 근거: 핀테크 리더, 2주+ 대기하던 10선 존 터치(0.15×ADR) 후 반등 확인($416→$423). 자본 19%
  (20% 캡). SL $409 = 박스상단$409+응집저점$411+10선$419 3중지지 아래, 0.58×ADR.
- 자금 출처: 같은날 실계좌 CRWD(사이버 약손) $188.1 정리분 → DAVE(핀테크 리더) = 약손→리더 +
  팩터 분산(사이버→핀테크).
- **7/22 종가 (진입 당일):** $423.7, 저가 $416.6(SL $409 미터치), 10선 $420.3 위 지지, -1.7%. 홀드.
  반사실 로그: 종가 20선 트레일이었다면 20선 $394.2(-7.0%)라 홀드 조건 — 즉 하드스탑 $409(-3.5%)가
  트레일보다 타이트하게 보호 중. 무너질 경우 하드스탑이 트레일보다 -3.5%p 덜 잃는 케이스가 됨(첫 표본).
- **반사실 추적(Claude 담당):** "하드스탑 없이 종가 20선 트레일이었다면?"을 브리핑마다 병행 기록
  → 하드스탑 이득 정량화용. DAVE 20선=$391 (진입가 대비 -8%, 하드SL $409보다 훨씬 아래).

## 페이퍼 계좌 전환 계획 (2026-07-20 확정)

**목적: 심리 검증이 아니라 전략(가설) 검증.** Jeonghun은 선물로 2년간 탐욕과 싸워온 이력이 있고,
하드룰이 있으면 실제 돈이 걸렸다고 룰을 어기지 않는다는 것이 본인 판단 — 따라서 "페이퍼는 심리를
못 시험한다"는 일반론은 이 케이스에 부적절. **지금 소액 실계좌의 목적도 원래 "가설·전략이 장기적으로
실제 작동하는가"였고, 그건 페이퍼로 검증 가능하다.**

**설정:**
- IBKR **페이퍼 계좌**, 잔고 **$1,000,000 기본값 → $50,000 정도로 리셋**(Client Portal → Paper
  Trading Account Reset). $1M 그대로 쓰면 사이징 감각이 완전히 달라짐.
- **하드스탑 ON으로 운용.** 이유: 페이퍼에서 검증되면 **stage-1로 돌아가지 않고 바로 stage-2로 간다.**
  따라서 검증 대상은 stage-2 환경(정수주 + 하드스탑)이어야 함.
- **정수주로 운용** (소수점 권한 불필요) — stage-2 환경과 일치하고, "20% 캡이 1주 값도 안 되는"
  문제도 사라짐.
- 체결은 슬리피지 없이 현재가에 채워지므로 **체결가는 낙관적**, 커미션은 실계좌 체계로 계산됨.
  결과 읽을 때 그만큼 할인.
- 실계좌 CRWD는 **그대로 유지·병행** (같은 시장에서 실제 vs 페이퍼 비교 데이터).

**★역할 분담:**
- **Jeonghun** = 하드스탑 켜고 정상 운용. **별도 기록 불필요** — Claude가 IBKR 계좌 툴로 직접 읽음.
- **Claude** = 매 브리핑마다 각 포지션의 **"하드스탑 없이 종가로 판단했다면?" 반사실(counterfactual)을
  병행 기록·누적** → 표본이 쌓이면 **"하드스탑이 확률적으로 얼마나 이득인가"**를 분석. stage-2 전환
  판단의 근거로 삼는다. (기존 백테스트의 최대 한계였던 "갭·무하드스탑 미반영"을 실제 셋업으로 메우는 작업.)

**✅ 2026-07-22 연결 완료:** 페이퍼 $20,000 세팅, 커넥터 연결 확인(get_account_summary/positions 정상 작동, 내가 직접 읽음). 가격 툴은 여전히 broken(Yahoo 사용). 실계좌 CRWD는 2026-07-22 $188.1 전량 정리(약손 청산, +이익). 

**연결 후 첫 세션 할 일:** ① $50,000 기준 사이징 재계산(종목당 캡·팩터캡·동시 포지션 수)
② 하드스탑 운용 규칙 확정(현재는 종가 수동이라 규칙 자체가 없음) ③ 와치리스트 중 조건 충족 종목
주문 초안 생성.

---

## 이벤트 캘린더 스냅샷 (2026-07-23 기준, 전부 ET)

**이미 발표 — 현 방어 로테이션의 원인**
- **미-이란 분쟁 확대 + 호르무즈 우려 → 유가 급등 → 국채금리 2026 고점** → 인플레 재점화·금리인하
  지연 우려 → 유틸/에너지/소재 아웃퍼폼, 기술/반도체 매도. (2026-07-22 XLU +2.2%, GLD +1.1%)
- **★반도체 공식 베어마켓 진입(2026-07-17)★** SOX가 6/22 사상최고 대비 -20.2%. 3월 저점→6월 고점
  +105% 급등의 되돌림. 촉매: Meta Compute 발표(자체 컴퓨트→칩 수요 감소 논리, 7/2 SOX -6.7%),
  Intel 18A-P 수율 지연(7거래일 -21%), 삼성 영업이익 19배인데 매출 컨센 미달로 -7%(KOSPI
  서킷브레이커), SK하이닉스 HBM 증설 속도조절, TSMC 호실적이나 CapEx 상향으로 -3%.
  → **판단 수정: "반도체 바닥 재출발(A)" 가설 보류.** 베어마켓 진입 직후의 기술적 반등으로 재분류,
  레짐상 🔴. 재진입 판단은 NVDA 실적(8/26) 이후로.
- 다이먼(JPM): 지정학·재정 리스크 과소평가 경고, 주식·장기국채 둘 다 안 사겠다.
- 7/22 장후: Alphabet·Tesla 실적 발표.

**곧 오는 것**
| 날짜 | 이벤트 | 볼 것 |
|---|---|---|
| 7/23 장후 | Intel | 반도체 심리 |
| **7/28~29** | **FOMC** (결정 7/29 14:00, Warsh 회견 14:30) | **점도표 없는 회차 → 어조가 전부.** 매파면 성장주 추가 타격 |
| **7/29 장후** | **Microsoft + Meta** (FOMC와 같은 날 = 이중 리스크) | AI capex 가이던스 |
| 7/30 장후 | Apple + Amazon | 빅테크 마무리 |
| **8/4** | **★DAVE 실적(보유 종목)★** | **갭 리스크. 8/1까지 청산/절반익절/홀드 결정** |
| 8/26 | NVIDIA | AI 서사 최종 판정. 반도체 재진입은 이 이후 |

**실행:** 7/29~30은 이틀에 3대 이벤트 겹침 → **신규 진입 금지, 사이즈 확대 금지**(갭은 스탑 무력화).
이번 시즌 S&P 이익성장 ~22% 중 절반이 AI capex 연동이고, 올해 시장은 실적 미스를 평소보다 가혹하게
처벌 중 → 양방향 변동성 큼.
