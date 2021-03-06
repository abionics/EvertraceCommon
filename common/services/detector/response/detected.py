from dataclasses import dataclass, field

from common.constants import UNKNOWN_ACCOUNT_NAME
from common.services.detector.response.feature import Feature


@dataclass(frozen=True, slots=True)
class Detected:
    name: str
    abi: dict | None = field(repr=False)
    deep_name: list[str]
    deep_properties: dict | None
    feature: Feature

    @classmethod
    def from_basic(cls, name: str, abi: dict | None, feature: Feature) -> 'Detected':
        return cls(name, abi, deep_name=[name], deep_properties=None, feature=feature)

    @classmethod
    def from_special(cls, name: str):
        return cls.from_basic(name, abi=None, feature=Feature.SPECIAL)

    @classmethod
    def unknown(cls) -> 'Detected':
        return cls.from_basic(UNKNOWN_ACCOUNT_NAME, abi=None, feature=Feature.UNKNOWN)
