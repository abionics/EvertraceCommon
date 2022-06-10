from common.abi.covert import convert_abis
from common.constants import USER_UNCHECKED_ABI_GROUP_NAME
from common.db.database import Database
from common.db.models import AbiGroup, Abi, Contract
from common.types import AbiList


def query_abi_registry(url: str) -> AbiList:
    database = Database(url)
    unchecked_group = _query_unchecked_group(database)
    abi_raw = database.session \
        .query(Abi.name, Abi.content) \
        .join(Contract, isouter=True) \
        .filter(Abi.group_id != unchecked_group.id) \
        .filter(Contract.abi_id == None) \
        .order_by(Abi.id)
    return convert_abis(abi_raw)


def _query_unchecked_group(database: Database) -> AbiGroup:
    return database.session. \
        query(AbiGroup). \
        filter_by(name=USER_UNCHECKED_ABI_GROUP_NAME). \
        first()
