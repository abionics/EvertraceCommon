from abc import ABC, abstractmethod

from pydantic.dataclasses import dataclass
from tvmbase.client import Client
from tvmbase.models.tvm.message import Message

from evertrace_common.decoder.response.direction import Direction


@dataclass(frozen=True)
class DecodeBaseParam(ABC):
    net: str

    @abstractmethod
    async def convert(self, client: Client) -> (str, str, Direction):
        pass

    @staticmethod
    def convert_message(message: Message) -> (str, str, Direction):
        direction = Direction.from_msg_type(message.data.msg_type)
        return message.idx, message.data.body, direction


@dataclass(frozen=True)
class DecodeBocParam(DecodeBaseParam):
    boc: str

    async def convert(self, client: Client) -> (str, str, Direction):
        message = await Message.from_boc(client, self.boc)
        return self.convert_message(message)


@dataclass(frozen=True)
class DecodeIdxParam(DecodeBaseParam):
    idx: str

    async def convert(self, client: Client) -> (str, str, Direction):
        message = await Message.from_idx(client, self.idx)
        return self.convert_message(message)


@dataclass(frozen=True)
class DecodePureParam(DecodeBaseParam):
    body: str
    direction: Direction = Direction.Internal

    async def convert(self, _: Client) -> (str, str, Direction):
        return None, self.body, self.direction
