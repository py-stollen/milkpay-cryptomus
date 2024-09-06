from ..types import Discount
from .base import CryptomusMethod


class SetPaymentMethodDiscount(
    CryptomusMethod[Discount],
    api_method="/v1/payment/discount/set",
    returning=Discount,
):
    """
    Source: https://doc.cryptomus.com/business/discount/set
    """

    currency: str
    network: str
    discount_percent: int
