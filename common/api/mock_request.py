from collections import namedtuple
from typing import cast

from fastapi import Request

MockRequestClient = namedtuple('MockRequestClient', 'host')
MockRequest = namedtuple('MockRequest', 'client')


def create_mock_request() -> Request:
    client = MockRequestClient(None)
    request = MockRequest(client)
    return cast(Request, request)
