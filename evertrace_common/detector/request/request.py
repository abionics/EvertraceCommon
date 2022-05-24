from abc import ABC, abstractmethod

from pydantic.dataclasses import dataclass
from tvmbase.client import Client
from tvmbase.models.tvm.account import Account


@dataclass(frozen=True)
class DetectBaseParam(ABC):
    net: str
    with_abi: bool

    @abstractmethod
    async def query_account(self, client: Client):
        pass


@dataclass(frozen=True)
class DetectBocParam(DetectBaseParam):
    boc: str

    async def query_account(self, client: Client) -> Account:
        return await Account.from_boc(client, self.boc)


@dataclass(frozen=True)
class DetectAddressParam(DetectBaseParam):
    address: str

    async def query_account(self, client: Client) -> Account:
        return await Account.from_address(client, self.address)
