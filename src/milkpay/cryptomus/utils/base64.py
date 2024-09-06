import base64


def validate_b64_image(value: str) -> bytes:
    raw_value: str = value.removeprefix("data:image/png;base64,")
    return base64.b64decode(raw_value)
