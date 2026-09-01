# ★★실행 환경 (절대 잊지 말 것) ★★
- **현재 디폴트 = IBKR paper account.** 모든 진입/사이징/손절 계산은 IBKR paper 기준(정수주, 하드스탑
  가능, 계좌 ~$19.8k). Toss/프랙셔널은 지금 논외 — 언급하지 말 것. 프랙셔널·소수점·Toss 제약을 사이징
  논의에 끌어오지 않는다.
- 검증단계 목적 = 전략 검증. IBKR MCP로 포지션/계좌 읽고, Yahoo EOD로 가격/차트.

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
  - ⚠️ **가격 툴 2026-07-28 세션에서 작동 확인** (`get_price_snapshot`/`get_price_history` 정수·불린
    파라미터 정상 호출, DAVE 데이터가 Yahoo와 일치 = 교차검증됨). 이전의 정수 직렬화 버그가 수정된
    것으로 보임. **단 1회 확인이라 다음 세션에 재검증 필요** — 안정 확인 전까진 "고쳐짐" 단정 보류.
    역할 분담: **장중 실시간·스냅샷·bid/ask = IBKR 우선 시도**, 안 되면 Yahoo. **백테스트·대량 일봉
    = Yahoo 유지**(캐시·split조정·대량조회 유리).
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
- **데이터 소스가 막히면 알아서 새 루트를 뚫는다**(Jeonghun 2026-07-25 지시). 가격=Yahoo EOD, 펀더=stockanalysis.com `/stocks/{T}/__data.json`(Yahoo quoteSummary는 crumb/401로 막힘). 막힐 때마다 대체 소스 탐색 후 STATUS에 갱신.
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

## ☀️ 내일(2026-08-06) 아침 브리핑 대기 항목 — Jeonghun 요청
1. **★매크로/뉴스 먼저 (web_search)** — 밤사이 왜 움직였나. 이란 협상 후속, 유가, 금리, DDOG 8/6 실적 결과.
   (Claude가 반복 누락 중 — 이번엔 반드시 첫 항목으로.)
2. **IBKR 로그인 장애 복구됐나** (8/5 IBKR 시스템 장애로 FTNT 진입 무산).
3. ~~FTNT $165~~ **깨짐 확정(8/5 종가 $164.1, 저$163.9)** → 진입후보 제외. $165 회복+유지 전까지 아님. 어제 IBKR장애 미진입이 방어가 됨.
4. **DDOG 8/6 실적**(장전) — observability 리더, 결과 확인.

## 시장 스냅샷 (2026-09-01 화 종가) — 2층 분석

**【대분류】** 소프트웨어 대군 오늘 -4.2% 조정이나 리딩 유지(정규화+2.97 vs 하드웨어(반도체) -0.99).
그동안 많이오른 SW 되돌림 + 시장전체 리스크오프.
**【소분류】** cyber 여전 1등(+3.00) but 오늘 -5.3%(어제 +5.8% 되돌림) > ai_sw(+2.70,-3.1%) > obs(+1.33).

- **매크로: 9월 첫날 리스크오프.** 나스닥 -1.03%(26,100, S&P의 3배 낙폭=메가캡기술 집중매도), S&P-0.71%,
  다우-419pt. 원인: 글로벌 채권금리 급등+유가급등(호르무즈 화물선공격)+9월 금리인상우려. VIX16.3.
  QQQ 50선 -0.3%(첫 이탈). = 시장전체 조정, CRWD/cyber 개별악재 아님.
- **★CRWD $215.1 +4.1%(+0.8ADR), 어제신고가$231서 -6.9% 되돌림.** +3ADR익절선$238 터치실패(어제$231까지).
  10선$211(+1.8% 위), 20선$207.6, BE$206.67(-3.9%). broken.
  **관리조정: 10선$211 종가이탈시 부분익절(모멘텀꺾임), 그위면 홀드. BE 하방지킴. 3-5일관찰 5일차.**
- **AVGO 9/2(내일) 진입안함**: 지는대군(HW -0.99)+조정장 = 부록42 상방제한+리스크. 대군로테이션상 SW가
  리딩인데 지는 HW 실적도박 안함.
- 교훈: 익절트리거($238) 못와서 홀드중 되돌림 = 결과론 자책말것(부록, 프로세스평가금지). 10선이탈 조건
  추가로 관리 강화. BE덕에 여전 +4.1%.

## 시장 스냅샷 (2026-08-31 월 종가) — 2층 분석

**【대분류: 대군 로테이션】** 소프트웨어 대군 압승 — 정규화 +3.94 (5일+15%/20일+28%) vs 하드웨어(반도체)
+0.74 (5일+2%). 부록42 로테이션 지속·강화. CRWD 홀드근거 견고.

**【소분류: SW대군 내 리더】** cyber 1등탈환(정규화+4.06 오늘+5.8% 5일+20%) > ai_software(+2.97 5일+12%)
> observability(+1.90). cyber↔ai_sw 하루하루 번갈아(부록43).

- **★Jeonghun 관찰(cyber 갭업후 안뻗음+ai_sw로 자금?) 검증: 금요일 일시현상.** 금 cyber-4.2% vs ai_sw
  +1.6%였으나 월 cyber+5.8% 재돌파로 뒤집힘. cyber 5일+20% > ai_sw+12% = 오히려 cyber가 자금 더받음.
  소분류 1등은 원래 번갈음, 큰그림 cyber 여전 최강.
- **★CRWD $231 신고가(+11.8%, +$422), BE스탑, 4일차.** 목고점$228 넘어 재돌파(안뻗은거 아님). +2.3ADR,
  10선+10%. **+3ADR 절반익절선 $238 근접(+3%) → 터치시 절반익절**(갭방어), 나머지 20선트레일.
- **AVGO 9/2(내일) = 지는 대군(HW)** — 실적좋아도 상방제한 가능(부록42). 진입 신중, 대군 로테이션 관점 우선.
- 국면: QQQ717 보합, 50선+1.0% 기울기+0.30%(둔화), VIX14.9. 소프트웨어 강세만 두드러짐.
- ※컨테이너리셋으로 engine/repo 재세팅+2층 프로토콜 재커밋(f42ed61).

## 시장 스냅샷 (2026-08-27 종가)

- **★예상 적중! cyber 꼴찌→1위 복귀 (하루 +17.9%).** 어제 7위(-2.65)→오늘 1위(+3.86). "원래1등이
  실적앞 리스크축소로 밀렸다 실적으로 복귀" 전제 완벽 실현. CRWD 진입 성공.
- **★CRWD 18주 @$206.67 → $228 (+10.3%, +$366).** +2.1ADR 도달, 전고점 $228 복귀. **★내일 절반 익절**
  (+2ADR 부분익절선 $226.5 넘음 + 전고점저항 + 하드스탑無 갭방어). 나머지 9주 20선 트레일 runner.
- **팩터순위(8/27): cyber+3.86 > 디파이+3.24 > ai_sw+2.67 > obs+1.99 > 금+0.54 > semi+0.53.** 성장주
  전반 강세 복귀(실적시즌 훈풍). QQQ+1.4%(721), VIX14.5, 50선+1.7%.
- **★셋업 빈도 분석 (네 질문): '실적강갭업 복귀'=연6.4회(드묾, 종목당0.4회/년). BUT 상위개념 '팩터
  순위복귀 사이클'=연25.5회(팩터당 2개월마다).** 실적갭업은 '복귀의 강한촉매 버전'일뿐, 본질은 팩터
  복귀. → 메인=팩터복귀 선점(연25.5회, 부록26 저점반등트랙 이미 이것), 실적갭업복귀=A급트리거(연6.4회,
  오면크게). 단 1승이라 과최적화 경계, 표본 쌓으며 검증.

## 시장 스냅샷 (2026-08-26 종가 + 포스트마켓 실적)

- **★실적 폭발(포스트마켓): OKTA +20%(매출$805M+11%,EPS$1.05 상회,가이던스 2번째상향,RPO+17%),
  CRWD +10%(매출$1.47B+26%,순신규ARR+51%,총ARR$5.84B+25%,가이던스상향), CRM 두자릿수, NVDA beat(but
  -1.6% 이미반영).** S&P500 2분기 실적 +50%YoY(2021이후 최고). AI 사이버보안 수요 강력.
- **장중은 조용(S&P 0.0%, QQQ +0.1%) — 실적 대기.** 50선기울기 +0.57%(계속 둔화), VIX15.2, 문샷구간
  진입임박(7/29후 20거래일).
- **★cyber 저점반등 트리거 임박(내일 목 확인):** 오늘 종가기준 cyber 5일 -4%였으나 포스트마켓 OKTA
  +20%/CRWD+10% 반영되면 내일 팩터 5일 양전환 가능 = 부록32 예측("CRWD실적이 cyber 트리거") 실현중.
- **★단 '진짜 저점' 아님:** cyber 저점대비 +95~131%(이미 2배+ 회복), 고점대비 -6~16%. semi/obs처럼
  '이미 회복'에 가까움(부록30 함정). = 순수 저점반등 아니라 '펀더강한 팩터의 실적 재상승'으로 봐야.
- **종목(부록32 강손+펀더): PANW(RS37,매출+31% 최강펀더)·CRWD(RS17,+26%,ARR+51%) 우선. OKTA(RS50
  최강+반등주도 but 성장+11% 낮음), FTNT(RS23).** 진입시 이미오른상태라 사이즈 신중.
- **내일 액션: cyber 5일 양전환 확인 → PANW/CRWD 저점반등(실은 실적재상승) 진입 검토, 단 +95% 올라와
  신중.** 문샷구간+실적시즌 강세면 갈래A(PLTR/ESTC) 병행 관찰.

## 시장 스냅샷 (2026-08-25 장중→종가)

- **★SNOW 청산 완료: $316.95, 실현 -$157.94 (-4.5%).** 실적(8/26) 전날 계획대로 청산 — 못뻗음(+2ADR
  $361까지 +13.6%) + 당일 -4.5% 10선이탈 + 무방비 실적홀드 부적절(갭 ±15-20%). 계좌 100% 현금.
- **국면: 엔비디아(수 8/26)+잭슨홀(금, Warsh 첫연설) 대기 관망 + 반도체 약세 + 무역갈등(캐나다 보복관세
  $200억 9/8발효).** 월 반도체급락(MU-5.8%), 화 반등시도. 엔비디아 서버가격인상=마진우려. 내일 PCE물가.
- **함정구간 19일차 끝자락. QQQ 50선 +0.2%(거의닿음), 기울기 +0.66%(계속둔화: +1.2→0.85→0.66).** VIX15.6.
  다음주 문샷구간(40일+) 진입, 엔비디아·잭슨홀이 분기점.
- **★팩터 지형변화: 디파이 폭발(+6.28, BTC주간+22%), ai_software 회복(+0.94, 지난주-0.43서 반등),
  semi 바닥근접(+0.03).** cyber -3.09 여전 약. → ai_sw 갈래A(PLTR/ESTC) 팩터 살아나는중.
- **저점반등 트리거 미발동:** MRVL 5일+13%나 거래량1.1(<1.2)+저점+49%(늦음), MU/NVDA 대기. 엔비디아
  실적이 semi 방향 결정.
- **★이번 검증사이클 종료: 3전 3정리 (PANW -7.5%, BLZE -0.94%, SNOW -4.5%), 합계 약 -$632(-3.2%).**
  전부 통제된 손실, 규칙대로 청산. 함정구간+로테이션 장에서 진입한 게 근본 원인(부록19-26 전략진화로 귀결).

## 시장 스냅샷 (2026-08-21 종가)

- **국면: 5일 하락 멈추고 반등(경기지표 4년래 최고).** S&P +0.43%(7674), 나스닥 +0.43%, 다우+518pt.
  나스닥100 5일연속하락 마감. but 금리 우려 지속, 성장→방어 로테이션 계속(헬스 주간+4% 모더나/머크
  흑색종백신, 금 3개월최고 $4569 5주연속). 다음주 잭슨홀(Warsh 매파우려)+수 엔비디아 실적 분수령.
- **함정구간 17일차. QQQ 50선 +0.7%(근접), 기울기 +0.85%(둔화중, 2주전 +1.2%서 내려옴).** VIX15.1.
  끝신호 아직없으나 경계.
- **★SNOW $332.8 +3.6%(손익+0.5% 플러스전환), flag, 10선+2.2%. 8/26실적 이틀뒤 → 월요일 청산결정.**
  +2ADR $361 못감(+8%). SL$308 -7.4%.
- **★워치리스트 태그 수정(Jeonghun 지적): PLTR·GTLB는 '초강손' 아님 = 오류.** PLTR 8/10급등후 $172-180
  응집중(밴드 12%→5%, flag)=초강손(응집없이감)과 모순. 실제 = "급등후 첫응집(갈래A)". 칼질장에 버티는
  종목 넣은것도 부록19 위반(칼질장엔 저점반등). → PLTR·GTLB는 팩터(ai_sw/obs) 재상승+응집돌파시 진입,
  지금 팩터약세(-0.43)라 대기.
- **금 온도계: 3개월최고 = 리스크오프 지속 = 성장주 진입 계속 조심.**

## 시장 스냅샷 (2026-08-20 종가)

- **국면: 월마트 -9%쇼크 + 금리재반등 + OpenAI부진으로 하락.** S&P -0.87%(7641), 나스닥 -1%, 다우 -703pt
  (-1.32%). 월마트 강한실적에도 미매출둔화(고유가 트레이드오프) -9%=4년래최악, 소비주 견인 하락. 재무부
  국채매입 효과 단기소멸→금리재반등(10년4.69%,30년5.24%). OpenAI 미지근 실적=AI하이퍼스케일러 하락.
  국가부채 $40조돌파. 시장 'iffy'.
- **★경계 커짐: QQQ 50선 +0.3%(거의닿음), VIX 16.0, 함정구간 16일차.** 50선기울기 +0.94%(아직+, 끝신호
  전은 아님). 내일 50선깨고 기울기 꺾이면 진짜 경계=2차조정 위험↑.
- **★포지션 정리: PANW 청산 $354.29 -$287(-7.5%)** — 20선이탈 능동청산, 오늘 cyber -3.3%로 잘뺌.
  **BLZE 손절 $16.66 -$186(-0.94% 갭)**. 두손실 -$473(-2.4%), 통제됨.
- **★SNOW 유일포지션 $321.3 -3.0%: 실적(8/26) 3일뒤 청산결정 필요.** 못뻗음(+2ADR $361까지 +12%),
  10선 -0.8% 이탈시작, 20선+2.7%. 무방비 실적홀드 부적절(못뻗음+10선이탈+시장위험 삼중). 계획대로
  8/24~25 청산 권고.
- **팩터: ai_software -0.28(SNOW 그나마 방어), semi -0.97, observability -2.92, cyber -4.74(완전붕괴,
  PANW 뺀게 정답).**

## 시장 스냅샷 (2026-08-19 종가)

- **국면: 금리진정으로 반등하나 기술→가치 로테이션 지속.** S&P +0.2%(3일 하락끝냄), QQQ -0.2%(기술 약세
  지속). ★재무부 장기국채 buyback 2배확대($2B→$4B+)→30년물 -10bp(5.18%). FOMC의사록 매파(여럿 인상선호).
  머크+10%/모더나급등(백신), 헬스/순환주 강세 vs 기술 XLK-1.9%. 트럼프 캐나다관세 3일유예, Target호조.
- **함정구간(15일차). QQQ 50선 +1.1%로 근접, 기울기 +1.01%(끝신호 아직없음).** VIX 15.2. 기술→가치
  로테이션이 성장주 역풍.
- **★BLZE 손절 완료: $18 체결(8/19 $16.88 급락), -$91=계좌-0.46%.** 계획대로(밑져야본전). ★희석리스크
  현실화(AI인프라 -5.9%+신주등록), 소액+타이트가 정답. 프로세스 승리(풀사이즈였으면 -1.3%+).
- **★PANW 심각: $359.76 -3.8%(손익-6.0%), 10선 -3.1% 이탈(첫 이탈), 20선 -0.5% 깨기직전, SL$347까지
  -3.5%만.** 진입논리(10선얹힘+추세) 상실. cyber 최약(-2.31). ★능동적 청산 검토(손절 기다리지말고).
- **SNOW $325 -0.1%: flag유지, 10선+0.2% 간신히, 20선+4.2%, SL$308 -5.2%. 8/26실적 5일뒤+못뻗음
  (+2ADR $361까지 +11%).** ai_software +3.4% 유일 반등.
- **팩터: ai_software +0.69(유일 반등), semi -1.09, AI인프라 -2.14, cyber -2.31(최약, PANW배경).**

## 시장 스냅샷 (2026-08-18 종가)

- **국면: 반도체 -5.5% 폭락 + 금리 2007년래최고 + 유가·이란으로 기술주 하락.** S&P -0.7%, 나스닥 -1.7%.
  30년물 5.32%(2007년래최고, AI기업 채권발행+인플레), 10년물 4.73%. 트럼프 "이란 경제고통+오만 폭격"
  브렌트$91. 방어주(헬스/유틸) 강세. 홈디포 실적 보합. 수요일 FOMC의사록, 목요일 월마트.
- **★7/29 조정후 14거래일 = 20-39일 함정구간 진입.** QQQ 50선 +1.3%로 근접(어제+3.1%), VIX 15.8오름,
  50선기울기 +1.05%(아직 끝신호 없음). 유가·이란·금리가 2차조정 트리거될지 주시.
- **★내 3포지션 다 약함(진입후 못뻗고 흘러내림):** PANW -2.3%(broken, 10선+0.1% 간신히, SL$347 -7.3%),
  SNOW -1.8%(flag유지, 10선+0.3%, SL$308 -5.3%, ★8/26실적 6일뒤 못뻗음→+2ADR 안오면 실적전 청산준비),
  BLZE -0.5%(소액 편함, 10선+3.1%).
- **팩터: semi 하루만에 -6.1% 폭락(어제1위서 추락, 반도체지수 -5.5%), AI인프라 -4.6%.** 어제 CRDO
  추격 안한게 정답(V반등꼭대기 회피). cyber +0.8%/ai_software +0.5%는 오늘 상대적 방어.
- **신규진입 절대없음(함정구간+금리리스크). 기존 포지션 관리 집중.**

## 시장 스냅샷 (2026-08-17 종가)

- **국면: 유가$90+이란 재점화로 조정.** S&P -0.5%(7745, 사상최고서 후퇴), 나스닥 -0.3%. 미-이란 MOU
  월요일 만료+이란 "공세전환/호르무즈 긴장고조" 경고+트럼프 "전쟁 안끝나". 브렌트 $90, 30년물 수십년래
  최고. 약한 소매판매(-0.6%)+소비심리 51급락. 수요일 FOMC의사록(3명 인상반대), 리테일실적주간, 잭슨홀.
- **상승장 건강: 50선기울기 +1.14%, 끝신호 전무.** VIX15.2. 7/29후 13거래일=곧 함정구간(20-39일)
  — 유가·이란이 2차조정 트리거될지 경계.
- **★내 3포지션 혼조:** PANW -1.9%(오늘-2.2%, cyber최약에 눌림, 10선+0.5% 간신히, SL$347 -7.7%여유,
  ★진입후 못뻗음 주의), SNOW -0.3%(오늘+0.4% 방어, flag유지, 10선위, SL$308, 8/26실적),
  BLZE +0.5%(오늘+1.9%, 소액 편함).
- **★팩터 로테이션 큰변화: semi 1위 등극(+2.5%, 정규화+1.72, 리더 CRDO+64%)** — 죽었던 반도체 재정렬
  신호, 우리가 지목한 CRDO가 실제리더로. cyber 최약 추락(-1.50, PANW팩터). AI인프라 +1.43(리더BLZE).
  observability -0.51, ai_software -1.00.
- **관리: PANW 계속 약하면 재평가. SNOW 8/26실적 관건. 신규진입 없음.**

## 시장 스냅샷 (2026-08-17 장중→종가, 3포지션 보유)

- **★3개 포지션 (3팩터 분산, 전부 손절 GTC):**
  - PANW 10주 @$382.88 (cyber), 현$379.4 -0.9%, SL$347
  - SNOW 11주 @$331.21 (ai_software), 현$333.2 +0.6%, SL$308, 익절$361(+2ADR), 8/26실적
  - BLZE 70주 @$19.30 (AI인프라, 소액7%/밑져야본전), SL$18(-6.6%,리스크0.46%), 9/9희석이벤트
  - 총노출 $8,810(44.5%), 현금 55%.
- **국면: AI트레이드(Anthropic 매출)가 견인, 지정학·리테일실적 관망.** S&P보합, 신고가근처. 50선기울기
  +1.16%(건강, 조정전조 아님 — 7/24 20선-3.4%/기울기-0.13%와 정반대). VIX15. 시장폭73%.
- **7/29 조정후 13거래일** = V반등. 문샷 40일문턱(9월중순), 곧 20-39일 함정구간. 문샷 OFF.
- **이번주 잭슨홀(8/27-29), 리테일실적(월마트등). SNOW 8/26 실적이 내 포지션 핵심.**

## 시장 스냅샷 (2026-08-12 종가, CPI날)

- **국면: CPI 통과 + AI인프라 실적 폭발로 상승.** S&P +0.3%, 나스닥 +0.5%. 7월 CPI 예상부합(헤드라인
  3.4%, 근원 2.5%=1월래 최저). 9월 연준 동결확률 60%로↑. 단 유가 $83+(호르무즈 기대감소)는 리스크.
- **★AI인프라 팩터 오늘 폭발**(+9.4%, 정규화 +1.74 1위 등극): NBIS+34% CRWV+19% SMCI+19% DELL+9.9%
  HPE+8.1%. 우리가 8/10 신설한 팩터가 실적시즌에 적중. **단 다 실적갭이라 nh높아도 broken(응집미완)
  =진입은 대기.**
- **상승장 건강: 50선기울기 +0.55%(어제 +0.21%서 강해짐), 끝신호 전무.** VIX 14.5. 200선 +11.4%위.
- **★7/29 조정저점 후 10거래일** = V반등초기. 문샷 문턱 40일(9월중순), 곧 20-39일 함정구간(8월하순~9월초).
  문샷 여전히 OFF, 견조주만.
- **★PANW +1.1%($387), CPI 잘넘김, 홀드.** 손절$347까지 -10.3%, 익절$418까지 +8.0%. 10선위 +5.9%.
- **팩터: AI인프라 1위(+1.74), cyber +1.52(내팩터 2위), ai_software +1.49(오늘-1.7% 쉬어감), semi
  +1.11(반등), observability +0.36.** 신규진입 없음, AI인프라 응집형성 대기.

## 시장 스냅샷 (2026-08-11 종가)

- **국면: CPI 대기 + 이란 재격화, 이틀째 숨고르기.** S&P -0.3%(사상최고서 2일째 소폭↓), 나스닥 -0.6%.
  기술주 약세(GOOGL -2.9%) 산업/소형주 강세(러셀 +0.3%). 유가 이란긴장에 반등. VIX 15.3. **★8/12밤
  CPI = 이번주 핵심관문.**
- **★내 포지션 PANW: 진입 첫날 +0.2%($383.8).** 시장 -0.3%일에 방어(10선위 +6.4%). 손절$347까지
  -9.6% 여유. 부분익절 $418(+2ADR)까지 +8.9%. 홀드, 액션없음.
- **팩터 정규화 둔화(CPI대기):** ai_software +1.89, cyber +1.32(내팩터, 상위유지), observability +0.98,
  semi/AI인프라 마이너스.
- **신규진입 없음** — CPI 앞두고 관망, PANW 하나로 충분.

## 시장 스냅샷 (2026-08-10 종가)

- **국면: 유가반등발 숨고르기.** S&P -0.06%(사상최고서 소폭후퇴). 이란-호르무즈 딜 불확실성 재부각
  (이란 "직접협상 아니다" vs 미국 "임박")→유가반등(WTI+0.8%,XLE+4.7%)→인플레우려, 10년물 4.71%.
  **CPI(수) 관문.** CoreWeave·Cisco·AMAT 실적 이번주.
- **★DDOG +11.5% 반등 = 8/6 소프트웨어쇼크 완전회복.** 부록10 "개별훼손은 팩터 안죽임" 확정
  (observability +5.7% 오늘최강). VRNS와 달리 DDOG 팩터는 살아있었음.
- **팩터: ai_software 1위 유지(+5.05).** observability +2.97(반등), cyber +2.81, semi +0.96(-3.4%
  약세지속), fintech -2.17(최약). 소프트웨어 3형제 강세.
- **SNOW $334.7 nh100 = 여전히 확장(watch), 응집 미완.** 6일간 $308→335 계속 상승, 10선$310·20선
  $294가 한참 아래. 횡보 시작 안함. +8/26 실적. 진입 아직.
- **★FTNT $164.2 = zone$165 회복 임박(-0.5%).** 며칠 이탈후 복귀중. $165 넘어 유지시 후보 복귀 검토. broken.
- **semi 판정유보(오늘-3.4%), fintech 최약. 진입 없음, CPI 대기.**

## 시장 스냅샷 (2026-08-07 종가, 주간 마감)

- **국면: 리스크온 재점화, S&P 사상최고(7,758).** 7월 고용 예상외 -23k(예상+83k) → 9월 인상우려
  완화 → "나쁜뉴스가 호재". VIX 14.9, 금리↓, 광범위 상승(336상승/167하락=건강). 주간 S&P+3.6%(4월來
  최고). 다음관문 = 다음주 CPI.
- **팩터: ai_software 압도적 1위(정규화 +5.25, 오늘+6%).** cyber +2.69, semi +2.33, observability
  +2.06(DDOG쇼크 하루만에 회복=개별문제였음 확인), fintech -0.04(유일약세).
- **SNOW $330.5 nh100 = ai_software 리더, 관찰 1순위.** BUT 확장중(watch, 응집미완)—$300~320에서
  10/20선 붙을때까지 횡보 완성 필요(Jeonghun 지적) + 8/26 실적. 진입 아직.
- **FTNT $159.6 = zone$165 -3.2% 이탈지속, 후보 밖.** DDOG $233.9(쇼크 갭소화, broken).
  NET $300.3 nh100(observability 부상하나 broken).
- **semi 주간 반등(CRDO+8%,MRVL+4%)하나 여전히 역배열/nh69~83, 판정유보.** NVDA만 정배열 nh95.
- **진입 없음** — 후보 다 확장이거나 실적대기. 관망. 다음 브리핑 = 월 8/10 개장후.

## 시장 스냅샷 (2026-08-03 종가)

- **국면: 리스크온(8/3 하루, 장중→종가 유지).** ★촉매: **①미국-이란 긴장 완화**(트럼프 대규모 공격
  취소+월요일부터 협상, 호르무즈 개방 협상)→**유가 -5~6% 급락**(7월 내내 시달린 전쟁 프리미엄 해소)
  **②7월 ISM 제조업 55.6 호조 ③10년물 -5bp 4.68%**(성장주 우호). 나스닥 +2.08%, 다우 사상최고.
  ★진짜 리더 = **AI 인프라**(CoreWeave +17%, Nebius +16%, Lumentum +9.7% = observability/ai_sw
  인접). ★**반도체는 또 이탈**(SOX -1.9%, MU·AVGO 하락) = semi 배제 재확인. **주의: 이란은 헤드라인
  촉매라 되돌림 가능**(협상결렬 시 유가 재급등) → 리스크온 실체는 있으나(ISM·금리·실적) 이란
  의존분 있어 '하루로 확정' 일러, 며칠 지속 확인 필요. VIX 15.86, SPY 200선 +8.1%·50선 회복, 유가 -5.5%(전쟁
  프리미엄 해소). "폭풍 후 순풍" 진행.
- **팩터 정규화 전부 양전환:** observability +4.18 · ai_software +3.10 · **cyber +2.70(0.63→급등,
  냉각 완전해제)** · fintech +0.73 · semi +0.05.
- **진입후보:** ①**FTNT** $163.2 — 실적무풍(7/29통과)+리스크온+사이버회복. **박스상단 $165 돌파만
  남음(-1.1% 아래).** 유일 실행 후보. ②**DDOG** $273.6 — 박스상단 $270 돌파 유지하나 **8/6 실적
  D-3라 진입불가.** ③**SNOW** $307.5 watch, 추격불가, 8/26 실적.
- **DAVE 8/4 실적** — 오늘 +7.1% 선반영 급등(기대 높아 beat해도 갭다운 위험). 포지션 없음, 관망.
- **다음 트리거: FTNT $165 종가/장중 돌파 → 진입 검토(실적 무풍이라 미리 진입 논리 적용 가능한
  유일 종목).**

## 시장 스냅샷 (2026-07-31 종가) — 다음 세션 브리핑 출발점

- **국면: 리스크온 복귀.** VIX 15.99(2주+ 만에 16 아래), 방어자산 일제 하락(로테이션 해제), SPY
  200선 +6.7%·50선 회복. FOMC(매파적 동결, 9월 인상 리스크 잔존)+빅테크 실적 무사 통과가 배경.
- **팩터 정규화 모멘텀:** observability +4.16(1위, DDOG) · megatech +3.13 · **cyber +0.67(양전환,
  냉각해제 초입)** · fintech −0.47 · semi −1.08(데드캣, 배제).
- **사이버 냉각 해제 초입:** 오늘 일제 반등(FTNT +5%, S +3.6%, CRWD +3%)이나 **전부 broken(응집
  미완)**. VRNS 실적갭 이탈 후 **FTNT·S가 새 리더 후보**(nh 97/96). 전환구간 판정유보 — 며칠 응집
  형성 확인 필요.
- **진입 후보 (둘 다 아직 응집 전, 진입 대기):** ① **DDOG**(observability 리더, nh97 정배열,
  차트게이트 통과, 매출성장 29.5%; broken=확장; **실적 8/6 장전**) ② **사이버 새 리더 FTNT/S**(응집
  완성 시). 
- **실적 지뢰: DAVE 8/4, DDOG 8/6** — 실적 전 진입 금지.
- **관망 유지 종목:** VRNS $40(실적갭 후 역배열, 갭소화) · DAVE $372.7(8/4 실적 앞두고 최악, 캔들11%)
  · semi 전반(배제).

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
| ~~7/28~29~~ 완료 | **FOMC(7/29): 금리 3.5~3.75% 동결(9-3, 반대 3명 전원 인상쪽=매파적). Warsh guidance 제거. 9월 인상 가능성 잔존. 7/30 빅테크 실적 안도 반등 SPY+1.7/QQQ+3.3** |
| ~~구~~ | ~~FOMC 상세~~ (결정 7/29 14:00, Warsh 회견 14:30) | **점도표 없는 회차 → 어조가 전부.** 매파면 성장주 추가 타격 |
| **7/29 장후** | **Microsoft + Meta** (FOMC와 같은 날 = 이중 리스크) | AI capex 가이던스 |
| 7/30 장후 | Apple + Amazon | 빅테크 마무리 |
| **8/4** | **★DAVE 실적(보유 종목)★** | **갭 리스크. 8/1까지 청산/절반익절/홀드 결정** |
| **8/6 장전** | **DDOG 실적(신규 후보)** | observability 리더, 실적 전 진입 금지 |
| 8/26 | NVIDIA | AI 서사 최종 판정. 반도체 재진입은 이 이후 |

**실행:** 7/29~30은 이틀에 3대 이벤트 겹침 → **신규 진입 금지, 사이즈 확대 금지**(갭은 스탑 무력화).
이번 시즌 S&P 이익성장 ~22% 중 절반이 AI capex 연동이고, 올해 시장은 실적 미스를 평소보다 가혹하게
처벌 중 → 양방향 변동성 큼.
