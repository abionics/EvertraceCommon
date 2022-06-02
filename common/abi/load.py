from common.api.service.abi_loader import AbiLoader
from common.types import AbiList


async def load_abis(api_url: str, hashes: list[str]) -> AbiList:
    abi_loader = AbiLoader(api_url)
    return await abi_loader.load_abis(hashes)
