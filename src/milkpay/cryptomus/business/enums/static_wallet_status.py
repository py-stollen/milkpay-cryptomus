from enum import Enum


class StaticWalletStatus(str, Enum):
    BLOCKED = "blocked"
    ACTIVE = "active"
    INACTIVE = "in_active"
