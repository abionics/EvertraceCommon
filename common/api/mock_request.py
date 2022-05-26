from collections import namedtuple

MockRequestClient = namedtuple('MockRequestClient', 'host')
MockRequest = namedtuple('MockRequest', 'client')


def create_mock_request() -> MockRequest:
    client = MockRequestClient(None)
    return MockRequest(client)
