from typing import Optional, Self

from pydantic import Field, model_validator
from stollen import StollenMethod
from stollen.enums import HTTPMethod
from stollen.types import StollenT

from ..client import Cryptomus


class CryptomusMethod(
    StollenMethod[StollenT, Cryptomus],
    http_method=HTTPMethod.POST,
    abstract=True,
):
    pass


class PayoutMethod(CryptomusMethod[StollenT], abstract=True):
    pass


class PublicMethod(CryptomusMethod[StollenT], abstract=True):
    pass


class WithUUIDMethod(CryptomusMethod[StollenT], abstract=True):
    uuid: Optional[str] = Field(default=None)
    order_id: Optional[str] = Field(default=None, min_length=1, max_length=128)

    @model_validator(mode="after")
    def post_validation(self) -> Self:
        if not self.uuid and not self.order_id:
            raise ValueError("Either uuid or order_id must be provided!")
        return self


class WithUUIDPayoutMethod(
    PayoutMethod[StollenT],
    WithUUIDMethod[StollenT],
    abstract=True,
):
    pass
