from enum import StrEnum


class ExchangeRateSource(StrEnum):
    BINANCE = "Binance"
    BINANCE_P2P = "BinanceP2P"
    EXMO = "Exmo"
    KUCOIN = "Kucoin"
    GARANTEXIO = "Garantexio"
