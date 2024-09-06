from decimal import Decimal

from .base import CryptomusObject


class BalanceUnit(CryptomusObject):
    uuid: str
    balance: Decimal
    currency_code: str
