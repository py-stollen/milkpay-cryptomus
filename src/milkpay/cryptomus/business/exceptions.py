from stollen.exceptions import StollenAPIError


class CryptomusError(Exception):
    pass


class CryptomusAPIError(StollenAPIError, CryptomusError):
    pass


class InvalidMerchantUUIDError(CryptomusAPIError):
    pass


class ValidationError(CryptomusAPIError):
    pass


class InternalServerError(CryptomusAPIError):
    pass


class MissingMerchantError(CryptomusError):
    pass


class MissingAPIKeyError(CryptomusError):
    pass
