from .base import CryptomusObject


class TransferResult(CryptomusObject):
    user_wallet_transaction_uuid: str
    user_wallet_balance: float
    merchant_transaction_uuid: str
    merchant_balance: float
