from typing import Any

from .base import WithUUIDMethod


class ResendWebhook(
    WithUUIDMethod[list[Any]],
    api_method="/v1/payment/resend",
    returning=list[Any],
):
    """
    Source: https://doc.cryptomus.com/business/payments/resend-webhook
    """
