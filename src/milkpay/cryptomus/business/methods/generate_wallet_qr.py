from ..types import QRCode
from .base import CryptomusMethod


class GenerateWalletQR(
    CryptomusMethod[QRCode],
    api_method="/v1/wallet/qr",
    returning=QRCode,
):
    """
    Source: https://doc.cryptomus.com/business/payments/qr-code-pay-form
    """

    wallet_address_uuid: str
