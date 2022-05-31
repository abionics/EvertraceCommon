from abc import ABC
from enum import Enum

from pydantic import BaseModel
from tonclient.types import SortDirection


class ExtractorClass(str, Enum):
    TINY = 'tiny'
    EXTENDED = 'extended'


class LoadBaseParam(ABC, BaseModel):
    extractor_class: ExtractorClass = ExtractorClass.TINY


class LoadGraphParam(LoadBaseParam):
    idx: str
    target: str | None = None


class LoadAccountParam(LoadBaseParam):
    target: str
    from_time: int
    limit: int | None
    sort_direction: SortDirection


class LoadPureParam(LoadBaseParam):
    messages: list[str]
    transactions: list[str]
