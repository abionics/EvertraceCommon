import json

from tonclient.types import AbiContract
from tvmbase.abi.converter import json_to_abi

from common.types import AbiDict


def load_abis(abis: AbiDict) -> dict[str, AbiContract]:
    loaded = dict()
    for key, abi in abis.items():
        abi_dict = json.loads(abi)
        loaded[key] = json_to_abi(abi_dict)
    return loaded
