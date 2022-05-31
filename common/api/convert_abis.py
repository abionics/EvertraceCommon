from tvmbase.abi.converter import json_to_abi

from common.types import AbiDictRaw, AbiDict


def convert_abis(abis: AbiDictRaw) -> AbiDict:
    loaded = dict()
    for name, abi in abis.items():
        loaded[name] = json_to_abi(abi)
    return loaded
