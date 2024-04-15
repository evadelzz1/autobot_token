from myUpbit import upbit
from myClass import MyUpbit

import time

myupbit = MyUpbit(upbit)

while True:
    try:
        # myupbit.watch_and_order("buy", "BTT/KRW", 10000, 3.6)
        myupbit.sell_market_price("BTT/KRW", 5)

    except Exception as e:
        print(e)
        exit(0)

    time.sleep(5)
