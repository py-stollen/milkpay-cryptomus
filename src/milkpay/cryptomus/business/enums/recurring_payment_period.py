from enum import Enum


class RecurringPaymentPeriod(str, Enum):
    WEEKLY = "weekly"
    MONTHLY = "montly"
    THREE_MONTH = "three_month"
