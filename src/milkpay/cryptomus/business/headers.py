from __future__ import annotations

from base64 import b64encode
from hashlib import md5
from typing import Any

from stollen import Stollen, StollenMethod
from stollen.enums import RequestFieldType
from stollen.requests.factory import BaseRequestFieldFactory
from stollen.requests.fields import Header, RequestField

from .exceptions import MissingMerchantError


class HeadersProvider(BaseRequestFieldFactory):
    def __call__(
        self,
        client: Stollen,
        method: StollenMethod[Any, Stollen],
    ) -> list[RequestField]:
        from .client import Cryptomus
        from .methods.base import PayoutMethod, PublicMethod

        if not isinstance(client, Cryptomus):
            raise RuntimeError("Got an unexpected client type instance.")

        if isinstance(method, PublicMethod):
            return []

        if client.merchant is None:
            raise MissingMerchantError(
                f"`{method.__class__.__name__}` request "
                f"can't be performed without a specified merchant UUID!"
            )

        dump: dict[str, Any] = method.model_dump()
        data: dict[str, Any] = {
            (field.serialization_alias or key): dump[field.serialization_alias or key]
            for key, field in method.model_fields.items()
            if not isinstance(field.json_schema_extra, dict)
            or (
                field.json_schema_extra.get("field_type", RequestFieldType.BODY)
                == RequestFieldType.BODY
            )
            if dump[field.serialization_alias or key] is not None
        }

        api_key: str = client.resolve_api_key(payout=isinstance(method, PayoutMethod))
        json_data: str = client.session.json_dumps(data) if data else ""
        sign_base: str = b64encode(json_data.encode()).decode() + api_key
        signature: str = md5(sign_base.encode()).hexdigest()  # noqa: S324

        return [
            Header(name="merchant", value=client.merchant),
            Header(name="sign", value=signature),
        ]
