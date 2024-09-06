from datetime import datetime
from typing import Optional

from .base import CryptomusObject


class RecurringPaymentInfo(CryptomusObject):
    uuid: str
    name: str
    amount: float
    currency: str
    payer_currency: str
    payer_amount_usd: float
    payer_amount: float
    url_callback: Optional[str] = None
    discount_days: Optional[int] = None
    discount_amount: Optional[float] = None
    end_of_discount: Optional[datetime] = None
    period: str
    status: str
    url: str
    last_pay_off: Optional[datetime] = None
    additional_data: Optional[str] = None
