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
        instance = self.session.query(Service).filter_by(name=name).first()
        if instance is None:
            instance = Service(name=name)
            self.session.add(instance)
            logger.success(f'Created service "{name}"')
        self.commit()
        return instance.id

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
            self.session.rollback()
            raise e
