from ..types import Discount
from .base import CryptomusMethod


class GetDiscountList(
    CryptomusMethod[list[Discount]],
    api_method="/v1/payment/discount/list",
    returning=list[Discount],
):
    """
    Source: https://doc.cryptomus.com/business/discount/list
    """
