"""
scanner_v3.py — 콜라매기 v3 셋업 스캐너 (trading_playbook_v3 기준)
매일 실행: python3 scanner_v3.py
종목 풀에서 v3 셋업 5조건 맞는 종목 + 셋업 임박(watch) 종목 출력. 지속약세 신호등 체크.
데이터: Yahoo EOD. look-ahead 없음(전일 종가까지로 판단).
"""
import json, time, urllib.request, sys
import numpy as np, pandas as pd

# ---- 종목 풀 (고변동 성장주). 자유롭게 추가/수정 ----
POOL = ["NVDA","AMD","AVGO","MRVL","CRDO","ALAB","MU","SMCI","ARM","TSM","QCOM","LRCX",
        "PLTR","SNOW","NET","DDOG","CRWD","PANW","ZS","MDB","S","GTLB","ESTC","DT","OKTA","FTNT",
        "TSLA","SHOP","ABNB","DASH","U","RBLX","AFRM","SOFI","COIN","HOOD","SQ","NU","TTD","APP",
        "META","AMZN","GOOGL","MSFT","AAPL","NFLX","CRM","NOW","ADBE","AI","PATH","IONQ","RKLB","OKLO","SMR","VRT","DELL","ANET","NBIS","CRWV"]

def fetch(ticker, days=400):
    p2=int(time.time()); p1=p2-days*86400
    url=f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?period1={p1}&period2={p2}&interval=1d"
    req=urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req,timeout=20) as r: j=json.loads(r.read())
    res=j["chart"]["result"][0]; q=res["indicators"]["quote"][0]
    df=pd.DataFrame({"Date":pd.to_datetime(res["timestamp"],unit="s"),
        "Open":q["open"],"High":q["high"],"Low":q["low"],"Close":q["close"]}).dropna().set_index("Date")
    return df

def check_setup(df):
    """v3 5조건 체크. 반환: (state, 상세) state=SETUP(돌파임박)/WATCH(응집완성,돌파대기)/None"""
    if len(df)<60: return None,{}
    c=df["Close"]; h=df["High"]; l=df["Low"]
    e10=c.ewm(span=10,adjust=False).mean(); e20=c.ewm(span=20,adjust=False).mean(); e50=c.ewm(span=50,adjust=False).mean()
    adr=((h/l-1)*100).rolling(20).mean()
    i=len(df)-1  # 최신봉(전일종가)
    # 1) EMA 정배열
    align = e10.iloc[i]>e20.iloc[i]>e50.iloc[i]
    # 2) 사전상승
    prior_rise = (c.iloc[i]/c.iloc[i-20]-1)*100
    # 3) 변동성 수축
    recent=(h.iloc[i-5:i+1].max()/l.iloc[i-5:i+1].min()-1)*100
    prev=(h.iloc[i-15:i-5].max()/l.iloc[i-15:i-5].min()-1)*100
    contract = recent <= prev*0.7 and recent < 2*adr.iloc[i]
    # 4) 20EMA 위
    above = c.iloc[i]>e20.iloc[i]
    # 5) 돌파 임박: 종가가 응집 고점의 97%+ (돌파 근접)
    box_hi=h.iloc[i-5:i+1].max()
    near_breakout = c.iloc[i] >= box_hi*0.97
    detail={"정배열":align,"사전상승%":round(prior_rise,0),"수축":contract,"20선위":above,
            "밴드%":round(recent,1),"ADR%":round(adr.iloc[i],1),"박스고점":round(box_hi,2),
            "종가":round(c.iloc[i],2),"손절(박스하단)":round(l.iloc[i-5:i+1].min(),2)}
    if align and prior_rise>=15 and contract and above:
        if near_breakout: return "SETUP", detail  # 돌파 임박
        else: return "WATCH", detail  # 응집 완성, 돌파 대기
    return None, detail

def regime_check():
    """지속약세장? SPY 최근60일중 200선아래 일수"""
    df=fetch("SPY",300); c=df["Close"]; ma200=c.rolling(200).mean()
    below=(c<ma200).astype(int); days=below.tail(60).sum()
    return days, ("지속약세(쉬기)" if days>=45 else "거래가능")

if __name__=="__main__":
    print("="*60)
    days,reg=regime_check()
    print(f"신호등: SPY 최근60일중 200선아래 {days}일 → {reg}")
    print("="*60)
    setups=[]; watches=[]
    for t in POOL:
        try:
            df=fetch(t)
            st,d=check_setup(df)
            if st=="SETUP": setups.append((t,d))
            elif st=="WATCH": watches.append((t,d))
        except Exception as ex:
            pass
    print(f"\n★★ SETUP (돌파 임박, 진입 준비) — {len(setups)}개")
    for t,d in setups:
        sl_pct=(d['손절(박스하단)']/d['종가']-1)*100
        print(f"  {t:<6} 종가${d['종가']} 돌파선${d['박스고점']} 손절${d['손절(박스하단)']}({sl_pct:+.1f}%) ADR{d['ADR%']}% 사전상승{d['사전상승%']:.0f}% 밴드{d['밴드%']}%")
    print(f"\n★ WATCH (응집 완성, 돌파 대기) — {len(watches)}개")
    for t,d in watches:
        print(f"  {t:<6} 종가${d['종가']} 돌파선${d['박스고점']} ADR{d['ADR%']}% 밴드{d['밴드%']}%")
    if not setups and not watches:
        print("\n(오늘 셋업 없음)")
