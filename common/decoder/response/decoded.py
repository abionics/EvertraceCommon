from dataclasses import dataclass

from common.constants import UNKNOWN_FUNCTION_NAME, UNKNOWN_ACCOUNT_NAME
from common.decoder.response.direction import Direction
from common.decoder.response.feature import Feature


@dataclass(frozen=True, slots=True)
class Decoded:
    method: str
    data: dict | None
    contract_name: str
    direction: Direction
    signature: bool
    headers: dict | None
    feature: Feature

    @classmethod
    def unknown(cls, direction: Direction) -> 'Decoded':
        return cls(
            UNKNOWN_FUNCTION_NAME,
            data=None,
            contract_name=UNKNOWN_ACCOUNT_NAME,
            direction=direction,
            signature=False,
            headers=None,
            feature=Feature.UNKNOWN,
        )
