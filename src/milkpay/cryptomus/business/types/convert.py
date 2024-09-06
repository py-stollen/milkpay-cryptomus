from typing import Optional

from .base import CryptomusObject, StrFloat


class Convert(CryptomusObject):
    to_currency: str
    commission: Optional[StrFloat] = None
    rate: StrFloat
    amount: StrFloat
