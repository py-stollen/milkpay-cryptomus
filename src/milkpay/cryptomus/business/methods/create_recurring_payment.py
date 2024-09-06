from typing import Optional

from pydantic import Field

from ..types import RecurringPaymentInfo
from ..types.base import StrFloat
from .base import CryptomusMethod


class CreateRecurringPayment(
    CryptomusMethod[RecurringPaymentInfo],
    api_method="/v1/recurrence/create",
    returning=RecurringPaymentInfo,
):
    """
    Source: https://doc.cryptomus.com/business/recurring/creating
    """

    amount: StrFloat
    currency: str
    name: str = Field(min_length=3, max_length=60)
    period: str
    to_currency: Optional[str] = None
    order_id: Optional[str] = Field(min_length=1, max_length=100)
    url_callback: Optional[str] = None
    discount_days: Optional[int] = Field(default=None, ge=1, le=365)
    discount_amount: Optional[StrFloat] = None
    additional_data: Optional[str] = None
