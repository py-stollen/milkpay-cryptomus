from enum import StrEnum, auto


class PayoutPriorityType(StrEnum):
    RECOMMENDED = auto()
    ECONOMY = auto()
    HIGH = auto()
    HIGHEST = auto()
