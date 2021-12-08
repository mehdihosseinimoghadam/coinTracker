import os
import json
import sys
from datetime import timedelta
import redis
import requests
from fastapi import FastAPI
import argparse




client = redis.StrictRedis(host=os.environ.get("REDIS_HOST"))


def get_coins_info_from_api(q: str):
    """get list of coins with ids and symbol from api"""

    URL = f"https://api.coingecko.com/api/v3/coins/{q}"
    r = requests.get(url=URL)
    if r.status_code==404:
        URL = "https://api.coingecko.com/api/v3/coins/list"
        r = requests.get(url=URL)
        json_directory = r.json()
        d = {}
        for key in json_directory:
            d[key["symbol"]] = key["id"]
        idx = d[q]
        URL = f"https://api.coingecko.com/api/v3/coins/{idx}"
        r = requests.get(url=URL)
        return r.json()

    return r.json()


def get_coins_info_from_cache(key: str) -> str:
    """Data from redis."""

    val = client.get(key)
    return val


def set_coins_info_to_cache(key: str, value: str) -> bool:
    """Data to redis."""

    state = client.set(key, value=value, )
    return state


def Track_coin(coin: str) -> dict:
    # First it looks for the data in redis cache
    data = get_coins_info_from_cache(key=coin)

    # If cache is found then serves the data from cache
    if data is not None:
        data = json.loads(data)
        data["cache"] = True
        return data

    else:
        # If cache is not found then sends request to the CoinGecko API
        data = get_coins_info_from_api(coin)

        # This block sets saves the respose to redis and serves it directly
        data["cache"] = False
        data = json.dumps(data)
        state = set_coins_info_to_cache(key=coin, value=data)

        if state is True:
            return json.loads(data)
        return data


app = FastAPI()


@app.get("/coin-tracker/{coin}")
def view(coin: str) -> dict:
    return Track_coin(coin)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Methos gets the live price of cryptos.')
    parser.add_argument('--symbol', dest='symbol',type=str, help='Symbol for crypto')
    
    args = parser.parse_args()
    print(get_coins_info_from_api(args.symbol))
                           