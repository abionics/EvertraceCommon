from dataclasses import dataclass, field

from evertrace_common.constants import UNKNOWN_ACCOUNT_NAME
from evertrace_common.detector.response.feature import Feature


@dataclass(frozen=True, slots=True)
class Detected:
    name: str
    abi: dict | None = field(repr=False)
    deep_name: list[str]
    deep_properties: dict | None
    feature: Feature

    @classmethod
    def from_casual(cls, name: str, abi: dict | None, feature: Feature):
        return cls(name, abi, deep_name=[name], deep_properties=None, feature=feature)

    @classmethod
    def from_name(cls, name: str, feature: Feature):
        return cls.from_casual(name, abi=None, feature=feature)

    @classmethod
    def unknown(cls) -> 'Detected':
        return cls.from_name(UNKNOWN_ACCOUNT_NAME, Feature.UNKNOWN)
