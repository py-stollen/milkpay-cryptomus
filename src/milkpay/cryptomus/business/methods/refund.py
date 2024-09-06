from typing import Any

from .base import WithUUIDMethod


class Refund(
    WithUUIDMethod[list[Any]],
    api_method="/v1/payment/refund",
    returning=list[Any],
):
    """
    Source: https://doc.cryptomus.com/business/payments/refund
    """

    address: str
    is_subtract: bool
