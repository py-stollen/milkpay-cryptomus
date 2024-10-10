from enum import Enum


class PayoutStatus(str, Enum):
    PROCESS = "process"
    CHECK = "check"
    PAID = "paid"
    FAIL = "fail"
    CANCEL = "cancel"
    SYSTEM_FAIL = "system_fail"
