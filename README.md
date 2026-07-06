# Stocks_US — Jeonghun's US-equity momentum research + tooling

**This repo is written for an AI assistant to read at the start of a session, not
for a human.** It lets any new Claude session resume the research and trading work
without re-deriving context. If you are that assistant, read this file, then
`STATUS.md`, then the handbooks.

---

## What this is
A hypergrowth-momentum (Qullamaggie-style) research program for US equities, run by
Jeonghun Kim, adapted to hard structural constraints (Toss Securities fractional
shares, **no hard stops**, Korea timezone = overnight gap exposure, once-per-day
decisions near the US close). Alongside live trading there is a quantitative research
track — the **"synchronization thesis"** — and its practical output, a **strongest-hand
scanner**.

## How to respond to "브리핑 해줘" / "brief me" in a new session
1. Read `STATUS.md` (current conclusions, open items, data policy, IBKR status).
2. Read the three handbooks in `handbook/` (prior research → channel study → synthesis).
3. Read `trading_playbook_v2.md` (the live-trading methodology).
4. **Run the scanner** if the user wants a market read:
   `cd engine && python3 scanner.py` (EOD data, no setup beyond `pip install pandas numpy`).
   Summarise: which name is the RS leader per factor, its state and breakaway, and
   remember the empirical conclusion — *the leader carries the runners; rank-2 is the
   worst group; co-rest is not a timing edge.*
   - **When surfacing a factor leader (strong hand) as a watchlist candidate, ALWAYS
     pair it with the same factor's weak hand (a lower-RS laggard)** so the user can
     compare co-movement, size the weak hand at ≤½ the strong, and read breakaway.
     The scanner already emits RS#1 and the laggards — report them as a pair.
5. Give a market/regime read + candidate leaders, then let the user drive. Entry,
   sizing and runner management follow `trading_playbook_v2.md`, not the scanner.

## Data policy (important)
- Use **end-of-day daily OHLC from Yahoo** (split-adjusted). It is free and low-usage;
  the scanner caches per ticker per day. **The data source is not important and does
  not need to be surfaced to the user.**
- Prefer Yahoo EOD for anything close-based (this is a close-based, once-per-day
  strategy — intraday live prices are not needed).
- The **IBKR MCP connector is broken** (it stringifies integer/boolean params, so
  `get_price_history` / `get_price_snapshot` fail; string-only tools like
  `search_contracts` still work). Do **not** rely on it for prices. Until Anthropic
  fixes it at the platform level, default to Yahoo / web search. See `STATUS.md`.
- If a domain is blocked, the container network setting may need "All domains".
  (stooq.com is permanently blocked from datacenter IPs — do not use it; Yahoo works.)
- **Corporate actions (splits/dividends) — check proactively.** Yahoo prices are
  **split-adjusted**, so a position's pre-split entry price will look off by the split
  ratio (e.g. CRWD did a 4:1 split effective 2026-07-02: pre-split ~$703 entry → $175.85
  adjusted; do not read the ~$194 print as a crash). When a recorded entry and the live
  price diverge by a round multiple, **assume a split first and verify (web) before
  alarming or acting** — convert the entry to the adjusted basis and move on. The
  assistant should surface/verify this kind of news itself, not ask the user.

## Repo map
```
README.md                     <- you are here (entry point + briefing protocol)
STATUS.md                     <- READ FIRST to resume: conclusions, open items, IBKR bug
trading_playbook_v2.md        <- live-trading methodology (regime, setup, exits, sizing)
handbook/
  01_synchronization_research.md  <- the thesis + empirical pipeline BEFORE the channel study
  02_channel_study.md             <- THIS study: 7-round eye-calibration -> converged label engine
  03_synthesis_and_model.md       <- merged conclusions + scanner-vs-prior criterion + actionable model
engine/
  strong_hand_engine.py       <- converged (v7) 7-state chart-state classifier (importable)
  scanner.py                  <- daily strongest-hand scanner (RS rank + breakaway + state)
  requirements.txt
```

## The one-paragraph summary (if you read nothing else)
The factor moves and rests together (confirmed: co-state lift ~2.0–2.8 across both a
cyber and a semiconductor cohort). Within a synchronized factor, the **relative-strength
leader (rank 1 by trailing 63-day return) captures the fat right tail** of returns —
the big runners come almost only from the leader, and requiring it to sit in a clean
consolidation does *not* help (it slightly dilutes). Waiting for the whole factor to
"rest together" (co-rest) is **not** a timing edge; if anything the leader breaking
*away* from the factor is the signal. So the actionable model is: identify a
synchronized factor → trade its RS leader → don't demand a clean base, don't wait for
co-rest permission → manage risk with the playbook's partial-profit + sizing rules
(there are no hard stops). Entry-time ambiguity between "still forming" states is
irreducible — that is the 5:5 nature of the strategy, not a labeling failure.
