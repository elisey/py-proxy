from settings import settings
from Libs.HttpParser import HttpHeader, BaseStream


class Request(BaseStream):
    """Implement Http request"""

    def __init__(self, header: HttpHeader) -> None:
        super().__init__(header)
        # self._header['Host'] = 'habr12.com'  # TODO from settings
        self._header['Host'] = settings.target_host
        self._header['Accept-Encoding'] = 'gzip'

    def __bytes__(self) -> bytes:
        return bytes(self._header)
