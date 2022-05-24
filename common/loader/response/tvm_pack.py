from dataclasses import dataclass
from typing import Type

from tvmbase.models.tvm import TvmType
from tvmbase.models.tvm.account import Account
from tvmbase.models.tvm.base import BaseTvm
from tvmbase.models.tvm.message import Message
from tvmbase.models.tvm.transaction import Transaction


@dataclass(frozen=True, slots=True)
class TvmPack:
    messages: dict[str, Message]
    transactions: dict[str, Transaction]
    accounts: dict[str, Account]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            messages=cls._from_dict(data['messages'], Message),
            transactions=cls._from_dict(data['transactions'], Transaction),
            accounts=cls._from_dict(data['accounts'], Account),
        )

    def to_dict(self) -> dict[str, dict]:
        return {
            'messages': self._to_dict(self.messages),
            'transactions': self._to_dict(self.transactions),
            'accounts': self._to_dict(self.accounts),
        }

    @staticmethod
    def _from_dict(data: dict, tvm_class: Type[BaseTvm]) -> dict[str, TvmType]:
        return {
            key: tvm_class.from_dict(dump)
            for key, dump in data.items()
        }

    @staticmethod
    def _to_dict(storage: dict[str, BaseTvm]) -> dict:
        return {
            key: value.to_dict()
            for key, value in storage.items()
        }
