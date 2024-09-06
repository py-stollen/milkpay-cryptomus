from .base import CryptomusObject
from .service_commission import ServiceCommission
from .service_limit import ServiceLimit


class Service(CryptomusObject):
    network: str
    currency: str
    is_available: bool
    limit: ServiceLimit
    commission: ServiceCommission
