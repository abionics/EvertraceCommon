from tvmbase.abi.converter import json_to_abi

from common.types import AbiListRaw, AbiList


def convert_abis(abis: AbiListRaw) -> AbiList:
    return [
        (name, json_to_abi(abi, mutate=True))
        for name, abi in abis
    ]
