from dataclasses import dataclass

from evertrace_common.constants import UNKNOWN_FUNCTION_NAME
from evertrace_common.decoder.response.direction import Direction
from evertrace_common.decoder.response.feature import Feature


@dataclass(frozen=True, slots=True)
class Decoded:
    method: str
    data: dict | None
    contract_name: str | None
    direction: Direction
    signature: bool
    headers: dict | None
    feature: Feature

    @classmethod
    def unknown(cls, direction: Direction) -> 'Decoded':
        return cls(
            UNKNOWN_FUNCTION_NAME,
            data=None,
            contract_name=None,
            direction=direction,
            signature=False,
            headers=None,
            feature=Feature.UNKNOWN,
        )
