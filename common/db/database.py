from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from common.db.models import Base, Service, Query


class Database:

    def __init__(self, url: str):
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)
        self.session = Session(bind=self.engine)

    def init_service(self, name: str):
        instance = self.session.query(Service).filter_by(name=name).first()
        if instance is None:
            service = Service(name=name)
            self.session.add(service)
            logger.success(f'Created service "{name}"')
        self.commit()

    def save_query(self, query: Query):
        self.session.add(query)
        self.commit()

    def commit(self):
        try:
            self.session.commit()
        except IntegrityError as e:
            logger.warning(f'Database exception {e}, trying to rollback')
            self.session.rollback()
        except Exception as e:
            self.session.rollback()
            raise e
