from typing import Generic, Optional

from pydantic import Field
from stollen.types import StollenT

from .base import CryptomusObject
from .pagination_info import PaginationInfo


class Pagination(CryptomusObject, Generic[StollenT]):
    merchant_uuid: Optional[str] = None
    items: list[StollenT]
    info: PaginationInfo = Field(alias="paginate")
