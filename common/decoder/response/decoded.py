from dataclasses import dataclass

from common.constants import UNKNOWN_FUNCTION_NAME, RECEIVE_FUNCTION_NAME, BOUNCED_FUNCTION_NAME, UNKNOWN_ACCOUNT_NAME
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
    def from_basic(cls, name: str, direction: Direction, feature: Feature) -> 'Decoded':
        return Decoded(
            name,
            data=None,
            contract_name=UNKNOWN_ACCOUNT_NAME,
            direction=direction,
            signature=False,
            headers=None,
            feature=feature,
        )

    @classmethod
    def receive(cls) -> 'Decoded':
        return cls.from_basic(RECEIVE_FUNCTION_NAME, Direction.Internal, Feature.SPECIAL)

    @classmethod
    def bounced(cls) -> 'Decoded':
        return cls.from_basic(BOUNCED_FUNCTION_NAME, Direction.Internal, Feature.SPECIAL)

    @classmethod
    def unknown(cls, direction: Direction) -> 'Decoded':
        return cls.from_basic(UNKNOWN_FUNCTION_NAME, direction, Feature.UNKNOWN)
