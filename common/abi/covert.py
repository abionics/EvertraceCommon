from tvmbase.abi.converter import json_to_abi

from common.types import AbiDictRaw, AbiDict


def convert_abis(abis: AbiDictRaw) -> AbiDict:
    return {
        name: json_to_abi(abi, mutate=True)
        for name, abi in abis.items()
    }
