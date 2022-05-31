from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import JSONB, CIDR
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AbiGroup(Base):
    __tablename__ = 'abi_group'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Abi(Base):
    __tablename__ = 'abi'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    hash = Column(String(64), nullable=False, index=True, unique=True)
    content = Column(JSONB, nullable=False)
    version = Column(String)
    group_id = Column(Integer, ForeignKey('abi_group.id'), nullable=False)


class ContractGroup(Base):
    __tablename__ = 'contract_group'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Contract(Base):
    __tablename__ = 'contract'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, unique=True)
    hash = Column(String, index=True)
    address = Column(String(66), index=True)
    abi_path = Column(String)
    class_name = Column(String)
    class_type = Column(String)
    group_id = Column(Integer, ForeignKey('contract_group.id'), nullable=False)


class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Query(Base):
    __tablename__ = 'query'
    id = Column(Integer, primary_key=True)
    identifier = Column(String(64), nullable=False)
    ip = Column(CIDR)
    method = Column(String, nullable=False)
    request = Column(JSONB, nullable=False)
    response = Column(JSONB, nullable=False)
    exception = Column(Boolean, nullable=False)
    traceback = Column(String)
    duration = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    service_id = Column(Integer, ForeignKey('service.id'), nullable=False, index=True)
