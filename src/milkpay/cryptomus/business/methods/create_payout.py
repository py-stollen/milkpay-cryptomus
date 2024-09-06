from typing import Optional

from pydantic import Field

from ..types import PayoutInfo
from ..types.base import StrFloat
from .base import PayoutMethod


class CreatePayout(
    PayoutMethod[PayoutInfo],
    api_method="/v1/payout",
    returning=PayoutInfo,
):
    """
    Source: https://doc.cryptomus.com/business/payouts/creating-payout
    """

    amount: StrFloat
    currency: str
    order_id: str = Field(min_length=1, max_length=100)
    address: str
    is_subtract: bool
    network: str
    url_callback: Optional[str] = None
    to_currency: Optional[str] = None
    course_source: Optional[str] = None
    from_currency: Optional[str] = None
    priority: Optional[str] = Field(default=None, min_length=4, max_length=11)
    memo: Optional[str] = Field(default=None, min_length=1, max_length=30)
