from .base import CryptomusObject


class ServiceCommission(CryptomusObject):
    fee_amount: float
    percent: float
