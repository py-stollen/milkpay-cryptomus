from stollen.enums import HTTPMethod
from stollen.requests.fields import PlaceholderField

from ..types import ExchangeRate
from .base import PublicMethod


class GetExchangeRates(
    PublicMethod[list[ExchangeRate]],
    http_method=HTTPMethod.GET,
    api_method="/v1/exchange-rate/{currency}/list",
    returning=list[ExchangeRate],
):
    """
    Source: https://doc.cryptomus.com/business/exchange-rates/list
    """

    currency: str = PlaceholderField()
