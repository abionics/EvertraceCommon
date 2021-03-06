from common.api.service.abi_loader import AbiLoader
from common.types import AbiList, AbiHashes


async def load_abis(api_url: str, abi_hashes: AbiHashes) -> AbiList:
    if len(abi_hashes) == 0:
        return list()
    abi_loader = AbiLoader(api_url, ignore_not_found=False)
    names, hashes = zip(*abi_hashes)
    abi_list = await abi_loader.load_abis(hashes)
    return [
        (name, abi)
        for name, (_, abi) in zip(names, abi_list)
    ]
