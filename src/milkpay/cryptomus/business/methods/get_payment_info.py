from ..types import PaymentInfo
from .base import WithUUIDMethod


class GetPaymentInfo(
    WithUUIDMethod[PaymentInfo],
    api_method="/v1/payment/info",
    returning=PaymentInfo,
):
    """
    Source: https://doc.cryptomus.com/business/payments/payment-information
    """
