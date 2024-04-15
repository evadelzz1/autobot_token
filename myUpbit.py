from dotenv import load_dotenv
import os
import ccxt

upbit = ccxt.upbit()

if not load_dotenv():    # load .env
    print("Could not load .env file or it is empty. Please check if it exists and is readable.",)
    exit(1)

upbit_access_key = os.getenv("UPBIT_ACCESS_KEY")
upbit_secret_key = os.getenv("UPBIT_SECRET_KEY")

upbit.apiKey = upbit_access_key
upbit.secret = upbit_secret_key