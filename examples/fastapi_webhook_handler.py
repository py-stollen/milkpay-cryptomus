from __future__ import annotations

import logging
from typing import Any, Final, Annotated

from fastapi import APIRouter, Body, HTTPException
from starlette.requests import Request

from milkpay.cryptomus.business import Cryptomus
from milkpay.cryptomus.business.types import PaymentUpdate

router: Final[APIRouter] = APIRouter()
logger: Final[logging.Logger] = logging.getLogger(name=__name__)


@router.post("/webhook/cryptomus/payments")
async def accept_cryptomus_payment(
    request: Request,
    update: Annotated[PaymentUpdate, Body()],
) -> Any:
    cryptomus: Cryptomus = request.app.state.cryptomus
    if not cryptomus.check_signature(
        body_text=(await request.body()).decode(),
        update=update,
    ):
        raise HTTPException(status_code=401, detail="Invalid signature")
    logger.info("Received payment with id %d", update.uuid)
