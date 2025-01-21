from typing import Optional

from pydantic import Field

from .base import CryptomusUpdate, StrFloat
from .convert import Convert


class PaymentUpdate(CryptomusUpdate):
    type: str
    uuid: str
    order_id: str
    amount: StrFloat
    payment_amount: Optional[StrFloat] = None
    payment_amount_usd: Optional[StrFloat] = None
    merchant_amount: Optional[StrFloat] = None
    commission: Optional[StrFloat] = None
    is_final: bool
    status: str
    from_address: Optional[str] = Field(default=None, alias="from")
    wallet_address_uuid: Optional[str] = None
    network: Optional[str] = None
    currency: str
    payer_currency: str
    payer_amount: StrFloat
    payer_amount_exchange_rate: Optional[StrFloat] = None
    additional_data: Optional[str] = None
    convert: Optional[Convert] = None
    txid: Optional[str] = None
