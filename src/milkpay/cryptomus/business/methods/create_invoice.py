from typing import Optional

from pydantic import Field

from ..types import Currency, PaymentInfo
from ..types.base import StrFloat
from .base import CryptomusMethod


class CreateInvoice(
    CryptomusMethod[PaymentInfo],
    api_method="/v1/payment",
    returning=PaymentInfo,
):
    """
    Source: https://doc.cryptomus.com/business/payments/creating-invoice
    """

    amount: StrFloat
    currency: str
    order_id: str = Field(min_length=1, max_length=128)
    network: Optional[str] = None
    url_return: Optional[str] = Field(default=None, min_length=6, max_length=255)
    url_success: Optional[str] = Field(default=None, min_length=6, max_length=255)
    url_callback: Optional[str] = Field(default=None, min_length=6, max_length=255)
    is_payment_multiple: Optional[bool] = None
    lifetime: Optional[int] = Field(default=None, ge=300, le=43200)
    to_currency: Optional[str] = None
    subtract: Optional[int] = Field(default=None, ge=0, le=100)
    accuracy_payment_percent: Optional[float] = Field(default=None, ge=0, le=5)
    currencies: Optional[list[Currency]] = None
    except_currencies: Optional[list[Currency]] = None
    course_source: Optional[str] = None
    from_referral_code: Optional[str] = None
    discount_percent: Optional[int] = Field(default=None, ge=-99, le=100)
    is_refresh: Optional[bool] = None
