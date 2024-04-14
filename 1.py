import ccxt
import time
from datetime import datetime

upbit = ccxt.upbit()

def getPrice(_ticker):
    infos = upbit.fetch_ticker(_ticker)
    price_close = infos['close']
    return price_close

def getPriceTest(_ticker):
    infos = upbit.fetch_ticker(_ticker)
    print("*" * 100)
    print(infos)

    print("*" * 100)
    print(f"# symbol : {infos['symbol']}")
    print(f"# close  : {infos['close']}")
    print(f"# high   : {infos['high']}")

while True:
    time.sleep(3)
    price = getPrice("XRP/KRW")
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] Price: {price}")

