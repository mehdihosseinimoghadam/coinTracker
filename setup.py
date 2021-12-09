from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Live Crypto Price API From CoinGecko'
# Setting up
setup(
    name="CryptoTrackee",
    version=VERSION,
    author="Mehdi Hosseini Moghadam, Hanie Poursina",
    author_email="<m.h.moghadam1996@gmail.com> , <hanieh.poursina@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'cryptocurrency', 'crypto price', 'coingecko', 'coin', 'crypro api'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)