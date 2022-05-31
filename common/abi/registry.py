from loguru import logger
from tvmbase.utils.singleton import SingletonMeta

from common.db.database import Database
from common.db.models import Abi
from common.types import AbiDict


class AbiRegistry(AbiDict, metaclass=SingletonMeta):

    def __init__(self, database_url: str):
        self.database_url = database_url
        self.setup()

    def setup(self, clear: bool = True):
        if clear:
            self.clear()
        abis = self._load_abis()
        self.update(abis)
        logger.success(f'Setup {len(abis)} abis from db with {clear=}, total count is {len(self)}')

    def _load_abis(self) -> AbiDict:
        database = Database(self.database_url)
        return database.session.query(Abi.name, Abi.content)
