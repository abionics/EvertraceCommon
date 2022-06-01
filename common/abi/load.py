from common.api.service.abi_storage import AbiStorage
from common.types import AbiDict


async def load_abis(url: str, hashes: list[str]) -> AbiDict:
    abi_storage = AbiStorage(url)
    return await abi_storage.load_abis(hashes)
