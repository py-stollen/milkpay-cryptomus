from ..types import TransferResult
from ..types.base import StrFloat
from .base import PayoutMethod


class TransferToBusiness(
    PayoutMethod[TransferResult],
    api_method="/v1/transfer/to-business",
    returning=TransferResult,
):
    """
    Source: https://doc.cryptomus.com/business/payouts/transfer-to-business
    """

    amount: StrFloat
    currency: str
