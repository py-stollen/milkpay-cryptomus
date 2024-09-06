from typing import Optional

from .base import CryptomusObject


class BasePayoutInfo(CryptomusObject):
    uuid: str
    amount: float
    currency: str
    network: str
    address: str
    txid: Optional[str] = None
    status: str
    is_final: bool
    balance: float
