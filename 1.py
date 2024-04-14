import ccxt

print("*" * 100)
# List
coinLists = ["비트코인", "이더리움", "리플"]
print(coinLists)
print(coinLists[0])
coinLists.append("보라")
print(coinLists)
coinLists.remove("보라")
print(coinLists)

print("*" * 100)
# dictonary
prices = {"low": 100, "high": 200, "close": 180}
print(f"# closed prices : {prices['close']}")

print("*" * 100)
upbit = ccxt.upbit()

print("*" * 100)
upbit.load_markets()

print("*" * 100)
print(upbit.symbols)

print("*" * 100)
infos = upbit.fetch_ticker("XRP/KRW")
print(infos)
print(f"# symbol : {infos['symbol']}")
print(f"# close  : {infos['close']}")
print(f"# high   : {infos['high']}")
