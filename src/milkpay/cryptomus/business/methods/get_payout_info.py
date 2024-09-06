from ..types import PayoutInfo
from .base import WithUUIDPayoutMethod


class GetPayoutInfo(
    WithUUIDPayoutMethod[PayoutInfo],
    api_method="/v1/payout/info",
    returning=PayoutInfo,
):
    """
    Source: https://doc.cryptomus.com/business/payouts/payout-information
    """
