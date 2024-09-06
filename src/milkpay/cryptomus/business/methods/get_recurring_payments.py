from typing import Optional

from stollen.requests.fields import QueryField

from ..types import Pagination, RecurringPaymentInfo
from .base import CryptomusMethod


class GetRecurringPayments(
    CryptomusMethod[Pagination[RecurringPaymentInfo]],
    api_method="/v1/recurrence/list",
    returning=Pagination[RecurringPaymentInfo],
):
    """
    Source: https://doc.cryptomus.com/business/recurring/list
    """

    cursor: Optional[str] = QueryField(default=None)
