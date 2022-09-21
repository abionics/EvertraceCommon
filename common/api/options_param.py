from pydantic import BaseModel
from tvmbase.client import Client
from tvmbase.models.network import NetworkFactory


class OptionsParam(BaseModel):
    identifier: str
    net: str | None = 'main'

    @classmethod
    def generate(cls, identifier: str) -> 'OptionsParam':
        return cls(identifier=identifier, net=None)

    def create_client(self, evercloud_key: str) -> Client:
        network = NetworkFactory(evercloud_key).from_name(self.net)
        return Client(network)
