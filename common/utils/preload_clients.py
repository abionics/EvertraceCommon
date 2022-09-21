from tvmbase.client import Client
from tvmbase.models.network import NetworkFactory


def preload_clients(evercloud_key: str) -> list[Client]:
    networks = NetworkFactory(evercloud_key).get_all()
    return [
        Client(network)
        for network in networks
    ]
