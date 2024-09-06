from __future__ import annotations

from base64 import b64encode
from hashlib import md5
from typing import TYPE_CHECKING, Any, Optional

from stollen import Stollen

from .exceptions import (
    CryptomusAPIError,
    InternalServerError,
    InvalidMerchantUUIDError,
    MissingAPIKeyError,
    ValidationError,
)
from .headers import HeadersProvider

if TYPE_CHECKING:
    from .types import (  # type: ignore
        BalanceResponse,
        BlockingWallet,
        Currency,
        Discount,
        ExchangeRate,
        Pagination,
        PaymentInfo,
        PayoutHistoryEntry,
        PayoutInfo,
        QRCode,
        RecurringPaymentInfo,
        RefundedWallet,
        Service,
        TransferResult,
        Wallet,
    )
    from .types.base import CryptomusUpdate


class Cryptomus(Stollen):
    merchant: Optional[str]
    api_key: Optional[str]
    payout_api_key: Optional[str]

    def __init__(
        self,
        merchant: Optional[str] = None,
        api_key: Optional[str] = None,
        payout_api_key: Optional[str] = None,
        **stollen_kwargs: Any,
    ) -> None:
        self.merchant = merchant
        self.api_key = api_key
        self.payout_api_key = payout_api_key
        super().__init__(
            base_url="https://api.cryptomus.com",
            global_request_fields=[HeadersProvider()],
            response_data_key=["result"],
            error_message_key=["message"],
            general_error_class=CryptomusAPIError,
            error_codes={
                401: InvalidMerchantUUIDError,
                422: ValidationError,
                500: InternalServerError,
            },
            **stollen_kwargs,
        )

    def check_signature(self, body_text: str, update: CryptomusUpdate) -> bool:
        from .types import PayoutUpdate

        api_key: str = self.resolve_api_key(payout=isinstance(update, PayoutUpdate))
        encoded_body: bytes = body_text.replace(f',"sign":{update.sign}', "").encode()
        sign_base: str = b64encode(encoded_body).decode() + api_key
        signature: str = md5(sign_base.encode()).hexdigest()  # noqa: S324

        return signature == update.sign

    def resolve_api_key(self, payout: bool = False) -> str:
        if payout:
            if self.payout_api_key is None:
                raise MissingAPIKeyError("Payout API key is not set")
            return self.payout_api_key
        if self.api_key is None:
            raise MissingAPIKeyError("API key is not set")
        return self.api_key

    async def block_wallet(
        self,
        *,
        uuid: Optional[str] = None,
        order_id: Optional[str] = None,
        is_force_refund: Optional[bool] = None,
    ) -> BlockingWallet:
        from .methods import BlockWallet

        call: BlockWallet = BlockWallet(
            uuid=uuid,
            order_id=order_id,
            is_force_refund=is_force_refund,
        )

        return await self(call)

    async def cancel_recurring_payment(
        self,
        *,
        uuid: Optional[str] = None,
        order_id: Optional[str] = None,
    ) -> RecurringPaymentInfo:
        from .methods import CancelRecurringPayment

        call: CancelRecurringPayment = CancelRecurringPayment(
            uuid=uuid,
            order_id=order_id,
        )

        return await self(call)

    async def create_invoice(
        self,
        *,
        amount: float,
        currency: str,
        order_id: str,
        network: Optional[str] = None,
        url_return: Optional[str] = None,
        url_success: Optional[str] = None,
        url_callback: Optional[str] = None,
        is_payment_multiple: Optional[bool] = None,
        lifetime: Optional[int] = None,
        to_currency: Optional[str] = None,
        subtract: Optional[int] = None,
        accuracy_payment_percent: Optional[float] = None,
        currencies: Optional[list[Currency]] = None,
        except_currencies: Optional[list[Currency]] = None,
        course_source: Optional[str] = None,
        from_referral_code: Optional[str] = None,
        discount_percent: Optional[int] = None,
        is_refresh: Optional[bool] = None,
    ) -> PaymentInfo:
        from .methods import CreateInvoice

        call: CreateInvoice = CreateInvoice(
            amount=amount,
            currency=currency,
            order_id=order_id,
            network=network,
            url_return=url_return,
            url_success=url_success,
            url_callback=url_callback,
            is_payment_multiple=is_payment_multiple,
            lifetime=lifetime,
            to_currency=to_currency,
            subtract=subtract,
            accuracy_payment_percent=accuracy_payment_percent,
            currencies=currencies,
            except_currencies=except_currencies,
            course_source=course_source,
            from_referral_code=from_referral_code,
            discount_percent=discount_percent,
            is_refresh=is_refresh,
        )

        return await self(call)

    async def create_payout(
        self,
        *,
        amount: float,
        currency: str,
        order_id: str,
        address: str,
        is_subtract: bool,
        network: str,
        url_callback: Optional[str] = None,
        to_currency: Optional[str] = None,
        course_source: Optional[str] = None,
        from_currency: Optional[str] = None,
        priority: Optional[str] = None,
        memo: Optional[str] = None,
    ) -> PayoutInfo:
        from .methods import CreatePayout

        call: CreatePayout = CreatePayout(
            amount=amount,
            currency=currency,
            order_id=order_id,
            address=address,
            is_subtract=is_subtract,
            network=network,
            url_callback=url_callback,
            to_currency=to_currency,
            course_source=course_source,
            from_currency=from_currency,
            priority=priority,
            memo=memo,
        )

        return await self(call)

    async def create_recurring_payment(
        self,
        *,
        amount: float,
        currency: str,
        name: str,
        period: str,
        order_id: Optional[str] = None,
        url_callback: Optional[str] = None,
        discount_days: Optional[int] = None,
        discount_amount: Optional[float] = None,
        additional_data: Optional[str] = None,
    ) -> RecurringPaymentInfo:
        from .methods import CreateRecurringPayment

        call: CreateRecurringPayment = CreateRecurringPayment(
            amount=amount,
            currency=currency,
            name=name,
            period=period,
            order_id=order_id,
            url_callback=url_callback,
            discount_days=discount_days,
            discount_amount=discount_amount,
            additional_data=additional_data,
        )

        return await self(call)

    async def create_wallet(
        self,
        *,
        currency: str,
        network: str,
        order_id: str,
        url_callback: Optional[str] = None,
        from_referral_code: Optional[str] = None,
    ) -> Wallet:
        from .methods import CreateWallet

        call: CreateWallet = CreateWallet(
            currency=currency,
            network=network,
            order_id=order_id,
            url_callback=url_callback,
            from_referral_code=from_referral_code,
        )

        return await self(call)

    async def generate_wallet_qr(self, *, wallet_address_uuid: str) -> QRCode:
        from .methods import GenerateWalletQR

        call: GenerateWalletQR = GenerateWalletQR(wallet_address_uuid=wallet_address_uuid)

        return await self(call)

    async def get_balance(self) -> list[BalanceResponse]:
        from .methods import GetBalance

        call: GetBalance = GetBalance()

        return await self(call)

    async def get_discount_list(self) -> list[Discount]:
        from .methods import GetDiscountList

        call: GetDiscountList = GetDiscountList()

        return await self(call)

    async def get_exchange_rates(self, *, currency: str) -> list[ExchangeRate]:
        from .methods import GetExchangeRates

        call: GetExchangeRates = GetExchangeRates(currency=currency)

        return await self(call)

    async def get_payment_history(
        self,
        *,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        cursor: Optional[str] = None,
    ) -> Pagination[PaymentInfo]:
        from .methods import GetPaymentHistory

        call: GetPaymentHistory = GetPaymentHistory(
            date_from=date_from,
            date_to=date_to,
            cursor=cursor,
        )

        return await self(call)

    async def get_payment_info(
        self,
        *,
        uuid: Optional[str] = None,
        order_id: Optional[str] = None,
    ) -> PaymentInfo:
        from .methods import GetPaymentInfo

        call: GetPaymentInfo = GetPaymentInfo(
            uuid=uuid,
            order_id=order_id,
        )

        return await self(call)

    async def get_payment_services(self) -> list[Service]:
        from .methods import GetPaymentServices

        call: GetPaymentServices = GetPaymentServices()

        return await self(call)

    async def get_payout_history(
        self,
        *,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        cursor: Optional[str] = None,
    ) -> Pagination[PayoutHistoryEntry]:
        from .methods import GetPayoutHistory

        call: GetPayoutHistory = GetPayoutHistory(
            date_from=date_from,
            date_to=date_to,
            cursor=cursor,
        )

        return await self(call)

    async def get_payout_info(
        self,
        *,
        uuid: Optional[str] = None,
        order_id: Optional[str] = None,
    ) -> PayoutInfo:
        from .methods import GetPayoutInfo

        call: GetPayoutInfo = GetPayoutInfo(
            uuid=uuid,
            order_id=order_id,
        )

        return await self(call)

    async def get_payout_services(self) -> list[Service]:
        from .methods import GetPayoutServices

        call: GetPayoutServices = GetPayoutServices()

        return await self(call)

    async def get_recurring_payment_info(
        self,
        *,
        uuid: Optional[str] = None,
        order_id: Optional[str] = None,
    ) -> RecurringPaymentInfo:
        from .methods import GetRecurringPaymentInfo

        call: GetRecurringPaymentInfo = GetRecurringPaymentInfo(
            uuid=uuid,
            order_id=order_id,
        )

        return await self(call)

    async def get_recurring_payments(
        self, *, cursor: Optional[str] = None
    ) -> Pagination[RecurringPaymentInfo]:
        from .methods import GetRecurringPayments

        call: GetRecurringPayments = GetRecurringPayments(cursor=cursor)

        return await self(call)

    async def refund(self, *, address: str, is_subtract: bool) -> list[Any]:
        from .methods import Refund

        call: Refund = Refund(address=address, is_subtract=is_subtract)

        return await self(call)

    async def refund_blocked_wallet(
        self,
        *,
        uuid: Optional[str] = None,
        order_id: Optional[str] = None,
        address: str,
    ) -> RefundedWallet:
        from .methods import RefundBlockedWallet

        call: RefundBlockedWallet = RefundBlockedWallet(
            uuid=uuid,
            order_id=order_id,
            address=address,
        )

        return await self(call)

    async def resend_webhook(
        self,
        *,
        uuid: Optional[str] = None,
        order_id: Optional[str] = None,
    ) -> list[Any]:
        from .methods import ResendWebhook

        call: ResendWebhook = ResendWebhook(
            uuid=uuid,
            order_id=order_id,
        )

        return await self(call)

    async def set_payment_method_discount(
        self, *, currency: str, network: str, discount_percent: int
    ) -> Discount:
        from .methods import SetPaymentMethodDiscount

        call: SetPaymentMethodDiscount = SetPaymentMethodDiscount(
            currency=currency, network=network, discount_percent=discount_percent
        )

        return await self(call)

    async def test_webhook(
        self,
        *,
        url_callback: str,
        currency: str,
        network: str,
        uuid: Optional[str] = None,
        order_id: Optional[str] = None,
        status: Optional[str] = None,
    ) -> list[Any]:
        from .methods import TestWebhook

        call: TestWebhook = TestWebhook(
            url_callback=url_callback,
            currency=currency,
            network=network,
            uuid=uuid,
            order_id=order_id,
            status=status,
        )

        return await self(call)

    async def transfer_to_personal(self, *, amount: float, currency: str) -> TransferResult:
        from .methods import TransferToPersonal

        call: TransferToPersonal = TransferToPersonal(amount=amount, currency=currency)

        return await self(call)

    async def transfer_to_business(self, *, amount: float, currency: str) -> TransferResult:
        from .methods import TransferToBusiness

        call: TransferToBusiness = TransferToBusiness(amount=amount, currency=currency)

        return await self(call)
