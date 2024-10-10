from enum import Enum


class PayoutPriorityType(str, Enum):
    RECOMMENDED = "recommended"
    ECONOMY = "economy"
    HIGH = "high"
    HIGHEST = "highest"
