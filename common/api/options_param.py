from pydantic import BaseModel
from tvmbase.client import Client
from tvmbase.models.network import Network


class OptionsParam(BaseModel):
    identifier: str | None = None
    net: str = 'main'

    def create_client(self) -> Client:
        network = Network.from_name(self.net)
        return Client(network)
