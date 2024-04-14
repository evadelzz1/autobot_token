import ccxt
import time
from datetime import datetime

upbit = ccxt.upbit()

def getPrice(_ticker):
    infos = upbit.fetch_ticker(_ticker)
    price_close = infos['close']
    return price_close


# symbols = ["BTC/KRW", "ETH/KRW"], "XRP/KRW"]
upbit.load_markets()
symbols = upbit.symbols

mySymbols = ["BTC/KRW", "ETH/KRW", "XRP/KRW"]

for symbol in symbols:
    if not symbol in mySymbols:
        continue
    
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] Closed Price - {symbol} : {getPrice(symbol)}")
    
    01:34:50