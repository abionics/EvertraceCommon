from typing import Iterable

from tonclient.types import AbiContract

AbiListRaw = Iterable[tuple[str, dict]]
AbiList = list[tuple[str, AbiContract]]
