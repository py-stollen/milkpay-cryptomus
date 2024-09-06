from .balance_unit import BalanceUnit
from .base import CryptomusObject


class Balance(CryptomusObject):
    merchant: list[BalanceUnit]
    user: list[BalanceUnit]
