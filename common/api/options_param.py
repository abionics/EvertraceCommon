from pydantic import BaseModel
from tvmbase.client import Client
from tvmbase.models.network import Network


class OptionsParam(BaseModel):
    identifier: str
    net: str | None = 'main'

    @classmethod
    def generate(cls, identifier: str) -> 'OptionsParam':
        return cls(identifier=identifier, net=None)

    def create_client(self) -> Client:
        network = Network.from_name(self.net)
        return Client(network)
