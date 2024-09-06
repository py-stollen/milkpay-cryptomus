from typing import Optional

from pydantic import Field

from .base import CryptomusUpdate, StrFloat
from .convert import Convert


class PaymentUpdate(CryptomusUpdate):
    type: str
    uuid: str
    order_id: str
    amount: StrFloat
    payment_amount: StrFloat
    payment_amount_usd: StrFloat
    merchant_amount: StrFloat
    commission: StrFloat
    is_final: bool
    status: str
    from_address: str = Field(alias="from")
    wallet_address_uuid: Optional[str] = None
    network: str
    currency: str
    payer_currency: str
    additional_data: Optional[str] = None
    convert: Optional[Convert] = None
    txid: Optional[str] = None
