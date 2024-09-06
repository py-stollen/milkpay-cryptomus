from typing import Optional

from .base import CryptomusObject


class Currency(CryptomusObject):
    currency: str
    network: Optional[str] = None
