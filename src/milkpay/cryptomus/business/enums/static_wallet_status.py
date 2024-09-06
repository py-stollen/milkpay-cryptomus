from enum import StrEnum


class StaticWalletStatus(StrEnum):
    BLOCKED = "blocked"
    ACTIVE = "active"
    INACTIVE = "in_active"
