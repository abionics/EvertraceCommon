from typing import Type

from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from common.db.models import Base, Service


class Database:
    ENGINES = dict()

    def __init__(self, url: str):
        if url not in self.ENGINES:
            self._create_engine(url)
        self.engine = self.ENGINES[url]
        self.session = Session(bind=self.engine)

    def _create_engine(self, url: str):
        engine = create_engine(url)
        Base.metadata.create_all(engine)
        self.ENGINES[url] = engine

    def init_service(self, name: str) -> int:
        service = self.get_or_create(Service, name=name)
        return service.id

    def get_or_create(self, class_type: Type[Base], **kwargs) -> Base:
        instance = self.session.query(class_type).filter_by(**kwargs).first()
        if instance is None:
            instance = class_type(**kwargs)
            self.save(instance)
            logger.success(f'Created {class_type.__name__} with data {kwargs}')
        return instance

    def save(self, instance: Base, commit: bool = True) -> bool:
        self.session.add(instance)
        if commit:
            return self.commit()
        return True

    def commit(self) -> bool:
        try:
            self.session.commit()
            return True
        except IntegrityError as e:
            logger.warning(f'Database exception {e}, trying to rollback')
            self.session.rollback()
            return False
        except Exception as e:
            logger.error(f'Database exception {e}')
            self.session.rollback()
            raise e

    def __del__(self):
        if self.session is not None:
            self.session.close()
            del self.session
