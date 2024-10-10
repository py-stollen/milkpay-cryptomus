from datetime import datetime
from typing import Union


def to_cryptomus_fmt(date: Union[datetime, str]) -> str:
    if isinstance(date, str):
        return date
    return date.strftime("%Y-%m-%d %H:%M:%S")
