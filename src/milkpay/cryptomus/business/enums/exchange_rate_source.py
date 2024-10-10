from enum import Enum


class ExchangeRateSource(str, Enum):
    BINANCE = "Binance"
    BINANCE_P2P = "BinanceP2P"
    EXMO = "Exmo"
    KUCOIN = "Kucoin"
    GARANTEXIO = "Garantexio"
