from datetime import datetime


def to_cryptomus_fmt(date: datetime | str) -> str:
    if isinstance(date, str):
        return date
    return date.strftime("%Y-%m-%d %H:%M:%S")
