from abc import ABC
from enum import Enum

from pydantic.dataclasses import dataclass
from tonclient.types import SortDirection


class ExtractorClass(str, Enum):
    TINY = 'tiny'
    EXTENDED = 'extended'


@dataclass(frozen=True)
class LoadBaseParam(ABC):
    net: str
    extractor_class: ExtractorClass


@dataclass(frozen=True)
class LoadGraphParam(LoadBaseParam):
    idx: str
    target: str | None


@dataclass(frozen=True)
class LoadAccountParam(LoadBaseParam):
    target: str
    from_time: int
    limit: int
    sort_direction: SortDirection


@dataclass(frozen=True)
class LoadPreparedParam(LoadBaseParam):
    messages: list[str]
    transactions: list[str]
