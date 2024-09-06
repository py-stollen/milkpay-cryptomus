from typing import Optional

from .base import CryptomusUpdate, StrFloat


class PayoutUpdate(CryptomusUpdate):
    type: str
    uuid: str
    order_id: str
    amount: StrFloat
    merchant_amount: StrFloat
    commission: StrFloat
    is_final: bool
    status: str
    txid: Optional[str] = None
    network: str
    payer_currency: str
    payer_amount: StrFloat
