from .balance import Balance
from .base import CryptomusObject


class BalanceResponse(CryptomusObject):
    balance: Balance
