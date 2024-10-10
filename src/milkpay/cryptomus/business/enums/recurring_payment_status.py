from enum import Enum


class RecurringPaymentStatus(str, Enum):
    WAIT_ACCEPT = "wait_accept"
    CANCEL_BY_MERCHANT = "cancel_by_merchant"
    ACTIVE = "active"
    CANCEL_BY_USER = "cancel_by_user"
