# engine/

- `strong_hand_engine.py` — converged v7 seven-state chart classifier. Import it:
  `import strong_hand_engine as E; d = E.label(E.fetch_yahoo("CRWD"))`
- `scanner.py` — daily strongest-hand scanner. Run: `python3 scanner.py [--csv out.csv]`.
  Edit `WATCHLIST` at the top to track your own factors/tickers.

Deps: `pip install -r requirements.txt` (pandas, numpy). Data = Yahoo EOD, cached in
`engine/data_cache/` per ticker per day. No API keys. IBKR connector is broken; not used.
