from enum import StrEnum, auto


class InvoiceStatus(StrEnum):
    CONFIRM_CHECK = auto()
    PAID = auto()
    PAID_OVER = auto()
    FAIL = auto()
    WRONG_AMOUNT = auto()
    CANCEL = auto()
    SYSTEM_FAIL = auto()
    REFUND_PROCESS = auto()
    REFUND_FAIL = auto()
    REFUND_PAID = auto()
