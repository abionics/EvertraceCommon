from abc import ABC
from enum import Enum

from pydantic import BaseModel
from tonclient.types import SortDirection


class ExtractorClass(str, Enum):
    TINY = 'tiny'
    EXTENDED = 'extended'


class LoadBaseParam(ABC, BaseModel):
    net: str
    extractor_class: ExtractorClass

    class Config:
        use_enum_values = True


class LoadGraphParam(LoadBaseParam):
    idx: str
    target: str | None


class LoadAccountParam(LoadBaseParam):
    target: str
    from_time: int
    limit: int
    sort_direction: SortDirection


class LoadPureParam(LoadBaseParam):
    messages: list[str]
    transactions: list[str]
