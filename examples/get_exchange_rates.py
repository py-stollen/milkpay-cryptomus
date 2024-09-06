import asyncio
import logging

from milkpay.cryptomus.business import Cryptomus
from milkpay.cryptomus.business.enums import Currency


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    cryptomus: Cryptomus = Cryptomus()
    for rate in await cryptomus.get_exchange_rates(currency=Currency.TON):
        logging.info(rate)
    await cryptomus.session.close()


if __name__ == "__main__":
    asyncio.run(main())
