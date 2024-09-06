from ..types import RecurringPaymentInfo
from .base import WithUUIDMethod


class GetRecurringPaymentInfo(
    WithUUIDMethod[RecurringPaymentInfo],
    api_method="/v1/recurrence/info",
    returning=RecurringPaymentInfo,
):
    """
    Source: https://doc.cryptomus.com/business/recurring/info
    """
