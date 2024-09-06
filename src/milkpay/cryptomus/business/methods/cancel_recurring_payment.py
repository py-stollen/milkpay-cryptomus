from ..types import RecurringPaymentInfo
from .base import WithUUIDMethod


class CancelRecurringPayment(
    WithUUIDMethod[RecurringPaymentInfo],
    api_method="/v1/recurrence/cancel",
    returning=RecurringPaymentInfo,
):
    """
    Source: https://doc.cryptomus.com/business/recurring/cancel
    """
