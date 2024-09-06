from datetime import datetime
from typing import Optional

from pydantic import Field

from .base import CryptomusObject, Image


class PaymentInfo(CryptomusObject):
    uuid: str
    order_id: str
    amount: float
    payment_amount: Optional[float] = None
    payer_amount: Optional[float] = None
    discount_percent: Optional[float] = None
    discount: Optional[float] = None
    payer_currency: Optional[str] = None
    currency: Optional[str] = None
    merchant_amount: Optional[float] = None
    network: Optional[str] = None
    address: Optional[str] = None
    from_address: Optional[str] = Field(alias="from")
    txid: Optional[str] = None
    payment_status: Optional[str] = None
    url: str
    expired_at: Optional[datetime] = None
    is_final: Optional[bool] = None
    additional_data: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    # Undocumented structure fields, use at your own risk
    status: Optional[str] = None
    payment_amount_usd: Optional[float] = None
    payer_amount_exchange_rate: Optional[float] = None
    comments: Optional[str] = None
    commission: Optional[float] = None
    address_qr_code: Optional[Image] = None
