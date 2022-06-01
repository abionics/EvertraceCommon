from urllib.parse import urljoin

from common.abi.covert import convert_abis
from common.services.abi_storage.request import LoadParam
from common.types import AbiDictRaw, AbiDict
from common.utils.fetch import fetch


class AbiLoader:

    def __init__(self, api_url: str, ignore_not_found: bool = False):
        self.api_url = api_url
        self.ignore_not_found = ignore_not_found

    async def load_abis(self, hashes: list[str]) -> AbiDict:
        param = LoadParam(hashes=hashes, ignore_not_found=self.ignore_not_found)
        abi_raw = await self._load_query(param)
        return convert_abis(abi_raw)

    async def _load_query(self, param: LoadParam) -> AbiDictRaw:
        url = urljoin(self.api_url, 'load')
        return await fetch(url, data={'param': param})
