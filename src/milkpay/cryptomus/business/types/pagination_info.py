from typing import Optional

from pydantic import Field

from .base import CryptomusObject


class PaginationInfo(CryptomusObject):
    count: int
    has_pages: bool = Field(alias="hasPages")
    next_cursor: Optional[str] = Field(alias="nextCursor")
    previous_cursor: Optional[str] = Field(alias="previousCursor")
    per_page: int = Field(alias="perPage")
