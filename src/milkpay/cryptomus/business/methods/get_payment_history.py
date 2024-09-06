from typing import Optional

from stollen.requests.fields import QueryField

from ..types import Pagination, PaymentInfo
from ..types.base import DateTime
from .base import CryptomusMethod


class GetPaymentHistory(
    CryptomusMethod[Pagination[PaymentInfo]],
    api_method="/v1/payment/list",
    returning=Pagination[PaymentInfo],
):
    """
    Source: https://doc.cryptomus.com/business/payments/payment-history
    """

    date_from: Optional[DateTime] = None
    date_to: Optional[DateTime] = None
    cursor: Optional[str] = QueryField(default=None)
