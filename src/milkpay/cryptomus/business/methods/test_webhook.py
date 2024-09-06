from typing import Any, Optional

from pydantic import Field

from .base import CryptomusMethod


class TestWebhook(
    CryptomusMethod[list[Any]],
    api_method="/v1/test-webhook/payment",
    returning=list[Any],
):
    """
    Source: https://doc.cryptomus.com/business/payments/testing-webhook
    """

    url_callback: str = Field(min_length=6, max_length=150)
    currency: str
    network: str
    uuid: Optional[str] = None
    order_id: Optional[str] = Field(default=None, min_length=1, max_length=32)
    status: Optional[str] = None
