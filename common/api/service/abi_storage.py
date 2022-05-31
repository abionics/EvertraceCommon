from urllib.parse import urljoin

from tvmbase.abi.converter import json_to_abi

from common.services.abi_storage.request import LoadParam
from common.types import AbiDictRaw, AbiDict
from common.utils.fetch import fetch


class AbiStorage:

    def __init__(self, url: str, ignore_not_found: bool = False):
        self.url = url
        self.ignore_not_found = ignore_not_found

    async def load_abis(self, hashes: list[str]) -> AbiDict:
        param = LoadParam(hashes=hashes, ignore_not_found=self.ignore_not_found)
        abis_raw = await self._load_query(param)
        return self._convert_abis(abis_raw)

    async def _load_query(self, param: LoadParam) -> AbiDictRaw:
        url = urljoin(self.url, 'load')
        return await fetch(url, data={'param': param})

    @staticmethod
    def _convert_abis(abis: AbiDictRaw) -> AbiDict:
        return {
            name: json_to_abi(abi)
            for name, abi in abis.items()
        }
