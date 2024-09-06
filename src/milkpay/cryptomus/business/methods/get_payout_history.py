from typing import Optional

from stollen.requests.fields import QueryField

from ..types import Pagination, PayoutHistoryEntry
from ..types.base import DateTime
from .base import PayoutMethod


class GetPayoutHistory(
    PayoutMethod[Pagination[PayoutHistoryEntry]],
    api_method="/v1/payout/list",
    returning=Pagination[PayoutHistoryEntry],
):
    """
    Source: https://doc.cryptomus.com/business/payouts/payout-history
    """

    date_from: Optional[DateTime] = None
    date_to: Optional[DateTime] = None
    cursor: Optional[str] = QueryField(default=None)
