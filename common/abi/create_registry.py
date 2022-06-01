from common.abi.covert import convert_abis
from common.db.database import Database
from common.db.models import Abi
from common.types import AbiDict


def create_abi_registry(database_url: str) -> AbiDict:
    database = Database(database_url)
    data = database.session.query(Abi.name, Abi.content)
    abi_raw = dict(data)
    return convert_abis(abi_raw)
