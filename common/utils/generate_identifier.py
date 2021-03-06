import datetime

from common.constants import IDENTIFIER_PREFIX


def generate_identifier(service_id: int, ip: str) -> str:
    timestamp = datetime.datetime.now(datetime.timezone.utc).timestamp()
    return f'{IDENTIFIER_PREFIX}-{timestamp:016.4f}-{service_id:02}-{ip}'
