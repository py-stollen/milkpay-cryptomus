from io import BytesIO

from .base import CryptomusObject, Image


class QRCode(CryptomusObject):
    image: Image

    def as_stream(self) -> BytesIO:
        return BytesIO(self.image)
