from abc import ABC, abstractmethod

from pydantic import BaseModel
from tvmbase.client import Client
from tvmbase.models.tvm.account import Account


class DetectBaseParam(ABC, BaseModel):
    net: str
    with_abi: bool

    @abstractmethod
    async def query_account(self, client: Client):
        pass


class DetectBocParam(DetectBaseParam):
    boc: str

    async def query_account(self, client: Client) -> Account:
        return await Account.from_boc(client, self.boc)


class DetectAddressParam(DetectBaseParam):
    address: str

    async def query_account(self, client: Client) -> Account:
        return await Account.from_address(client, self.address)
