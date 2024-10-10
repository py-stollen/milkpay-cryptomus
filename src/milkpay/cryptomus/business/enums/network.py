from enum import Enum


class Network(str, Enum):
    """
    Source: https://doc.cryptomus.com/business/reference
    """

    ARBITRUM = "arbitrum"
    AVALANCHE = "avalanche"
    BCH = "bch"
    BSC = "bsc"
    BTC = "btc"
    DASH = "dash"
    DOGE = "doge"
    ETH = "eth"
    LTC = "ltc"
    POLYGON = "polygon"
    SOL = "sol"
    TON = "ton"
    TRON = "tron"
    XMR = "xmr"
