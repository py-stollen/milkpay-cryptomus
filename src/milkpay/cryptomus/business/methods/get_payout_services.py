from ..types.service import Service
from .base import PayoutMethod


class GetPayoutServices(
    PayoutMethod[list[Service]],
    api_method="/v1/payout/services",
    returning=list[Service],
):
    """
    Source: https://doc.cryptomus.com/business/payouts/list-of-services
    """
