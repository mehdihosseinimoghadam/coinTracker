# CryptoTrackerr 
## Live Crypto Price API From CoinGecko

[![N|Solid](https://cdn-icons.flaticon.com/png/512/2272/premium/2272825.png?token=exp=1639032339~hmac=d9c787f97b1d8a220688b164a2a63064)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

CryptoTrackerr is a wrapper package to get live crypto prices from CoinGecko

## Features

- Easy to use
- Fast
- Accurate


## Pip Installation
 For installation simply use:

```sh
pip install CryptoTrackerr
```

## Usage


```py
from CryptoTrackerpy import get_coins_info
get_coins_info("Crypto Symbol")
```

Use case for BTC

```py
from CryptoTrackerpy import get_coins_info
get_coins_info("btc")

out:
{'additional_notices': [],
 'asset_platform_id': None,
 'block_time_in_minutes': 10,
 'categories': ['Cryptocurrency'],
 'coingecko_rank': 2,
 'coingecko_score': 80.366,
 'community_data': {'facebook_likes': None,
  'reddit_accounts_active_48h': 3707,
  'reddit_average_comments_48h': 1029.778,
  'reddit_average_posts_48h': 7.444,
  'reddit_subscribers': 3650683,
  'telegram_channel_user_count': None,
  'twitter_followers': 3949316},
 'community_score': 70.897,
 'country_origin': '',
 'description': {'ar': '',
...
```

## Run with CLI

```sh
python3 main.py --symbol btc
```

## Docker

Docker of CryptoTrackerr is avaliable with redis, so for the first time when you get a query, redis will cache the price 

```sh
docker-compose up
```



## Authors

| Name | Github | Home Page |
| ------ | ------ | ------|
| Mehdi Hosseini Moghadam | [https://github.com/mehdihosseinimoghadam][PlDb] |https://www.linkedin.com/in/mehdi-hosseini-moghadam-384912198/|
| Hanie Poursina | [https://github.com/HaniePoursina][PlGh] | http://haniepoursina.ir/

## Github

Source is avaliable at
[https://github.com/mehdihosseinimoghadam/coinTracker][PlGh]



## License

MIT

**Free Software, Hell Yeah!**


