from common.abi.covert import convert_abis
from common.db.database import Database
from common.db.models import Abi
from common.types import AbiList


def create_abi_registry(database_url: str) -> AbiList:
    database = Database(database_url)
    abi_raw = database.session.query(Abi.name, Abi.content)
    return convert_abis(abi_raw)
