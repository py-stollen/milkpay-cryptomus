from .base import CryptomusObject


class ServiceLimit(CryptomusObject):
    min_amount: float
    max_amount: float
