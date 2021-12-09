import os
import json
import requests


def get_coins_info(q: str):
    """get list of coins with ids and symbol from api"""

    URL = f"https://api.coingecko.com/api/v3/coins/{q}"
    r = requests.get(url=URL)
    if r.status_code==404:
        URL = "https://api.coingecko.com/api/v3/coins/list"
        r = requests.get(url=URL)
        json_directory = r.json()
        # print(json_directory)
        d = {}
        for key in json_directory:
            d[key["symbol"]] = key["id"]

        idx = d[q]
        URL = f"https://api.coingecko.com/api/v3/coins/{idx}"
        r = requests.get(url=URL)
        return r.json()

    return r.json()


