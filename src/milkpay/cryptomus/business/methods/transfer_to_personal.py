from ..types import TransferResult
from ..types.base import StrFloat
from .base import PayoutMethod


class TransferToPersonal(
    PayoutMethod[TransferResult],
    api_method="/v1/transfer/to-personal",
    returning=TransferResult,
):
    """
    Source: https://doc.cryptomus.com/business/payouts/transfer-to-personal
    """

    amount: StrFloat
    currency: str
