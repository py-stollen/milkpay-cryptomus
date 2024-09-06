from ..types import BalanceResponse
from .base import CryptomusMethod


class GetBalance(
    CryptomusMethod[list[BalanceResponse]],
    api_method="/v1/balance",
    returning=list[BalanceResponse],
):
    """
    Source: https://doc.cryptomus.com/business/balance
    """
