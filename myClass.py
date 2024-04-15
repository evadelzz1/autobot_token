from datetime import datetime

class MyUpbit():
    def __init__(self, _upbit):
        self.upbit = _upbit
        self.isBuy = False
        self.isBuyCount = 0
        self.isBuyMaxCount = 5
        
    def getPrice(self, _ticker):
        infos = self.upbit.fetch_ticker(_ticker)
        price_close = infos['close']
        return price_close

    def watch_and_order(self, _orderType, _ticker, _orderAmount, _watch_percent):
        infos = self.upbit.fetch_ticker(_ticker)
        price_close = infos['close']            # 종가
        percent = infos['percentage'] * 100     # 전일 대비 변화량
        rounded_percent = round(percent, 6)
        nowDate = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        print(f"[{nowDate}] [{_ticker}] Current Price : {price_close:15.6f}, Daily fluctuation rate : {rounded_percent:10.6f}%, Watch Rate : {_watch_percent:10.6f}%")

        if percent < _watch_percent and not self.isBuy:
            self.upbit.create_market_order(_ticker, _orderType, _orderAmount, 1)
            self.isBuy = True
            exit(0)

    def sell_market_price(self, _ticker, _orderCount):
        infos = self.upbit.fetch_ticker(_ticker)
        price_close = infos['close']            # 종가
        percent = infos['percentage'] * 100     # 전일 대비 변화량
        rounded_percent = round(percent, 6)
        nowDate = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        print(f"[{nowDate}] [{_ticker}] Current Price : {price_close:15.6f}, Daily fluctuation rate : {rounded_percent:10.6f}%, Sell Count : {_orderCount}")

        self.upbit.create_market_order(_ticker, "sell", _orderCount)
            
    def watch_and_order_many(self, _orderType, _ticker, _orderAmount, _watch_percent):
        infos = self.upbit.fetch_ticker(_ticker)
        price_close = infos['close']            # 종가
        percent = infos['percentage'] * 100     # 전일 대비 변화량
        rounded_percent = round(percent, 6)
        print(f"[{nowDate}] [{_ticker}] Current Price : {price_close:15.6f}, Daily fluctuation rate : {rounded_percent:10.6f}%, Watch Rate : {_watch_percent:10.6f}%")

        if percent < _watch_percent and self.isBuyCount < self.isBuyMaxCount:
            self.upbit.create_market_order(_ticker, _orderType, _orderAmount, -1)
            self.isBuyCount = self.isBuyCount + 1
            if self.isBuyCount == self.isBuyMaxCount:
                exit(0)