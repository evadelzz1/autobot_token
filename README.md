# Autobot-token

소스코드 다운로드

    git clone https://github.com/evadelzz1/autotrading_coin.git


python 가상환경 activate 및 필요한 라이브러리 설치

    cd ./autotrading_coin

    pyenv versions

    pyenv local 3.11.6

    # pyenv install -list
    # pyenv install 3.11.6
    # pyenv local 3.11.6

    python -m venv .venv

    source .venv/bin/activate

    python -V   # 3.11.6

    pip install -r requirements.txt

코드 실행

    echo "UPBIT_ACCESS_KEY=..." >> .env
    echo "UPBIT_SECRET_KEY=..." >> .env

    python main.py

python 가상환경 deactivate

    deactivate

Reference
- 코인 자동매매 by 장도강 : [Youtube](https://www.youtube.com/watch?v=ktnZeL-gWw4), [Blog](https://velog.io/@jack_intheboxx/autotradingbasic2)
- 회계사가 직접 만든 자동매매 by 야근하는 회계사 : [Youtube](https://www.youtube.com/watch?v=jgdriEmharc)
- Tradingview : [Link](https://kr.tradingview.com/pricing/)