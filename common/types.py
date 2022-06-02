from tonclient.types import AbiContract

AbiListRaw = list[tuple[str, dict]]
AbiList = list[tuple[str, AbiContract]]
AbiHashes = list[tuple[str, str]]  # name, hash
