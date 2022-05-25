from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from common.constants import SERVICES
from common.db.models import Base, Service, Query


class Database:

    def __init__(self, url: str):
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)
        self.session = Session(bind=self.engine)

    def init_services(self):
        for name in SERVICES:
            service = Service(name=name)
            self.session.merge(service)

    def save_query(self, query: Query):
        self.session.add(query)
        self.commit()

    def commit(self):
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
        except Exception as e:
            self.session.rollback()
            raise e
