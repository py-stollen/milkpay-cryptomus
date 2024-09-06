from typing import Optional

from pydantic import Field

from ..types import RefundedWallet
from .base import WithUUIDMethod


class RefundBlockedWallet(
    WithUUIDMethod[RefundedWallet],
    api_method="/v1/wallet/blocked-address-refunds",
    returning=RefundedWallet,
):
    """
    Source: https://doc.cryptomus.com/business/payments/refundblocked
    """

    order_id: Optional[str] = Field(default=None, min_length=1, max_length=32)
    address: str = Field(min_length=10, max_length=128)
