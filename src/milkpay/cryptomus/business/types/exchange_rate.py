from pydantic import Field

from .base import CryptomusObject


class ExchangeRate(CryptomusObject):
    from_: str = Field(alias="from")
    to: str
    course: float
