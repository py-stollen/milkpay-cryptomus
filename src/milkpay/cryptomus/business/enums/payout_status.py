from enum import StrEnum, auto


class PayoutStatus(StrEnum):
    PROCESS = auto()
    CHECK = auto()
    PAID = auto()
    FAIL = auto()
    CANCEL = auto()
    SYSTEM_FAIL = auto()
