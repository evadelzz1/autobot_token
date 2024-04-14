import ccxt
import os
from dotenv import load_dotenv

isBuy = False

upbit = ccxt.upbit()

if not load_dotenv():    # load .env
    print("Could not load .env file or it is empty. Please check if it exists and is readable.",)
    exit(1)

upbit_access_key = os.getenv("UPBIT_ACCESS_KEY")
upbit_secret_key = os.getenv("UPBIT_SECRET_KEY")
# print(upbit_access_key)
# print(upbit_secret_key)
# exit(0)

upbit.apiKey = upbit_access_key
upbit.secret = upbit_secret_key

def getPrice(_ticker):
    infos = upbit.fetch_ticker(_ticker)
    price_close = infos['close']
    return price_close

def watch_and_order(_ticker):
    global isBuy
    infos = upbit.fetch_ticker(_ticker)
    price_close = infos['close']
    percent = infos['percentage'] * 100
    rounded_percent = round(percent, 2)
    print(f"현재 코인의 가격은 {price_close} 원이고, 전일대비 {rounded_percent}% 입니다.")

    if percent < -3 and not isBuy:
        upbit.create_market_order("ALGO/KRW", "buy", 1000, 1)
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

