from typing import Optional

from pydantic import Field

from ..types import Wallet
from .base import CryptomusMethod


class CreateWallet(
    CryptomusMethod[Wallet],
    api_method="/v1/wallet",
    returning=Wallet,
):
    """
    Source: https://doc.cryptomus.com/business/payments/creating-static
    """

    currency: str
    network: str
    order_id: str = Field(min_length=1, max_length=100)
    url_callback: Optional[str] = Field(default=None, min_length=6, max_length=255)
    from_referral_code: Optional[str] = None
