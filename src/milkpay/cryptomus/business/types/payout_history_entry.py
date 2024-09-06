from datetime import datetime

from .base_payout_info import BasePayoutInfo


class PayoutHistoryEntry(BasePayoutInfo):
    created_at: datetime
    updated_at: datetime
