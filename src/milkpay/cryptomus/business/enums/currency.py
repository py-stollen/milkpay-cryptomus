from enum import Enum


class Currency(str, Enum):
    """
    Source: https://doc.cryptomus.com/business/reference
    """

    USDT = "USDT"
    USDC = "USDC"
    ETH = "ETH"
    AVAX = "AVAX"
    BCH = "BCH"
    CGPT = "CGPT"
    DAI = "DAI"
    BNB = "BNB"
    BTC = "BTC"
    DASH = "DASH"
    DOGE = "DOGE"
    VERSE = "VERSE"
    MATIC = "MATIC"
    SHIB = "SHIB"
    LTC = "LTC"
    CRMS = "CRMS"
    SOL = "SOL"
    TON = "TON"
    TRX = "TRX"
    XMR = "XMR"
