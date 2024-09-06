from enum import StrEnum, auto


class RecurringPaymentStatus(StrEnum):
    WAIT_ACCEPT = auto()
    CANCEL_BY_MERCHANT = auto()
    ACTIVE = auto()
    CANCEL_BY_USER = auto()
