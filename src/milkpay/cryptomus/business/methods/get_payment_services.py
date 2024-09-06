from ..types.service import Service
from .base import CryptomusMethod


class GetPaymentServices(
    CryptomusMethod[list[Service]],
    api_method="/v1/payment/services",
    returning=list[Service],
):
    """
    Source: https://doc.cryptomus.com/business/payments/list-of-services
    """
