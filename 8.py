from myUpbit import upbit

class MyUpbit():
    def __init__(self, _upbit):
        print('# 객체 생성')
        self.upbit = _upbit
        self.isBuy = False
        
    def getPrice(self, _ticker):
        infos = self.upbit.fetch_ticker(_ticker)
        price_close = infos['close']
        return price_close

    def watch_and_order(self, _ticker, _orderAmount):
        infos = self.upbit.fetch_ticker(_ticker)
        price_close = infos['close']            # 종가
        percent = infos['percentage'] * 100     # 전일 대비 변화량
        rounded_percent = round(percent, 6)
        print(f"[{_ticker}] Current Price : {price_close}, Daily fluctuation rate : {rounded_percent}%")

        if percent < -3 and not isBuy:
            self.upbit.create_market_order(_ticker, "buy", _orderAmount, 1)
            self.isBuy = True

myupbit = MyUpbit(upbit)
print(myupbit.getPrice("XRP/KRW"))
myupbit.watch_and_order("XRP/KRW", 10000)