from typing import Optional

from pydantic import Field

from ..types import BlockingWallet
from .base import WithUUIDMethod


class BlockWallet(
    WithUUIDMethod[BlockingWallet],
    api_method="/v1/wallet/block-address",
    returning=BlockingWallet,
):
    """
    Source: https://doc.cryptomus.com/business/payments/block-wallet
    """

    order_id: Optional[str] = Field(default=None, min_length=1, max_length=32)
    is_force_refund: Optional[bool] = None
