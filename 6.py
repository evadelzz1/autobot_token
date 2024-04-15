from myUpbit import upbit

isBuy = False

def getPrice(_ticker):
    infos = upbit.fetch_ticker(_ticker)
    price_close = infos['close']
    return price_close

def watch_and_order(_ticker):
    global isBuy
    infos = upbit.fetch_ticker(_ticker)
    price_close = infos['close']            # 종가
    percent = infos['percentage'] * 100     # 전일 대비 변화량
    rounded_percent = round(percent, 2)
    print(f"[{_ticker}] Current Price : {price_close}, Daily fluctuation rate : {rounded_percent}%")

    if percent < -3 and not isBuy:
        upbit.create_market_order(_ticker, "buy", 1000, 1)
        isBuy = True 

watch_and_order("XRP/KRW")
exit(0)

try:
    # 시장가 주문 : 업비트, 최소 주문금액 5,000원
    upbit.create_market_order("ALGO/KRW", "buy", 1000, 1)
    upbit.create_market_order("ALGO/KRW", "sell", 1000, 1)

    # 지정가 주문
    upbit.create_limit_order("ALGO/KRW", "buy", 10, 600)    # 600원에 10개를 주문넣음
    upbit.create_limit_order("ALGO/KRW", "sell", 10, 600)

except Exception as e:
    print(e)

