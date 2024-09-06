from .base_payout_info import BasePayoutInfo


class PayoutInfo(BasePayoutInfo):
    payer_currency: str
    payer_amount: float
