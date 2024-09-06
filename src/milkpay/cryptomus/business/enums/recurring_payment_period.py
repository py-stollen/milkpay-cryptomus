from enum import StrEnum, auto


class RecurringPaymentPeriod(StrEnum):
    WEEKLY = auto()
    MONTHLY = auto()
    THREE_MONTH = auto()
