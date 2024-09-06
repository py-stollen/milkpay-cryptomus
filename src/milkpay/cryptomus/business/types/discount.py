from .base import CryptomusObject


class Discount(CryptomusObject):
    currency: str
    network: str
    discount: int
