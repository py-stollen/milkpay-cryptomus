from .base import CryptomusObject


class Wallet(CryptomusObject):
    wallet_uuid: str
    uuid: str
    address: str
    network: str
    currency: str
    url: str
