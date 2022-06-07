from typing import Type

from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from common.db.models import Base, Service


class Database:

    def __init__(self, url: str):
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)
        self.session = Session(bind=self.engine)

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

    def save(self, instance: Base) -> bool:
        self.session.add(instance)
        return self.commit()

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
