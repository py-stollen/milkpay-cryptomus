from enum import Enum


class InvoiceType(str, Enum):
    WALLET = "wallet"
    UUID = "uuid"
