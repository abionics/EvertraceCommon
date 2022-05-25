import inspect
import time
from typing import Callable

from fastapi import Request
from loguru import logger
from pydantic import BaseModel

from common.db.database import Database
from common.db.models import Query


def endpoint(service_id: int, version: str, db_url: str):
    def wrapper(function: Callable):
        async def wrapped(_: Request, **kwargs) -> dict:
            start_time = time.time()
            ip = _.client.host
            query = Query(ip=ip, method=function.__name__, request=_to_dict(kwargs), service_id=service_id)
            try:
                result = await function(_, **kwargs)
                query.exception = False
                response = create_response(version, exception=False, result=result)
            except Exception as e:
                logger.exception(e)
                reason = str(e)
                query.exception = True
                query.exception_reason = reason
                response = create_response(version, exception=True, reason=reason)
            finish_time = time.time()
            query.response = response
            query.duration = finish_time - start_time
            db = Database(db_url)
            db.save_query(query)
            return response

        wrapped.__signature__ = inspect.signature(function)
        return wrapped

    return wrapper


def _to_dict(data: dict) -> dict:
    result = dict()
    for key, value in data.items():
        if isinstance(value, BaseModel):
            value = value.dict()
        result[key] = value
    return result


def create_response(version: str, exception: bool, **kwargs) -> dict:
    return {
        'version': version,
        'exception': exception,
        **kwargs,
    }
