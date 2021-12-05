import json
import sys
from datetime import timedelta

import wikipedia
import httpx
import redis
import requests
from fastapi import FastAPI




def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host="localhost",
            port=6379,
            password="ubuntu",
            db=0,
            socket_timeout=5,
        )
        ping = client.ping()
        if ping is True:
            return client
    except redis.AuthenticationError:
        print("AuthenticationError")
        sys.exit(1)


client = redis_connect()


def get_routes_from_api(q: str):
    """Data from mapbox api."""

    URL = "https://api.coingecko.com/api/v3/coins/list"
    r = requests.get(url = URL)
    data1 = r.json()

    d = {}
    for i in data1:       ##### Must be a better way to to this #####
      d[i["symbol"]]=i["id"]
    

########################################################
# api-endpoint
    idx = d[q]
    print("----------------------------------------",idx)
    URL = f"https://api.coingecko.com/api/v3/coins/{idx}"


    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    
    # extracting data in json format



    return r.json()


def get_routes_from_cache(key: str) -> str:
    """Data from redis."""

    val = client.get(key)
    return val


def set_routes_to_cache(key: str, value: str) -> bool:
    """Data to redis."""

    state = client.setex(key, timedelta(seconds=3600), value=value,)
    return state


def route_optima(coordinates: str) -> dict:

    # First it looks for the data in redis cache
    data = get_routes_from_cache(key=coordinates)

    # If cache is found then serves the data from cache
    if data is not None:
        data = json.loads(data)
        data["cache"] = True
        return data

    else:
        # If cache is not found then sends request to the MapBox API
        data = get_routes_from_api(coordinates)

        # This block sets saves the respose to redis and serves it directly
        if data.get("code") == "Ok":
            data["cache"] = False
            data = json.dumps(data)
            state = set_routes_to_cache(key=coordinates, value=data)

            if state is True:
                return json.loads(data)
        return data


app = FastAPI()


@app.get("/route-optima/{coordinates}")
def view(coordinates: str) -> dict:
    """This will wrap our original route optimization API and
    incorporate Redis Caching. You'll only expose this API to
    the end user. """

    # coordinates = "90.3866,23.7182;90.3742,23.7461"

    return route_optima(coordinates)