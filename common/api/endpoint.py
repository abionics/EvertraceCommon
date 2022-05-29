import inspect
import time
import traceback
from typing import Callable, Any

from fastapi import Request
from loguru import logger
from pydantic import BaseModel

from common.api.options_param import OptionsParam
from common.db.database import Database
from common.db.models import Query
from common.utils.recursive_convert import recursive_convert


def endpoint(service_id: int, version: str, db_url: str):
    def wrapper(function: Callable):
        async def wrapped(request: Request, options: OptionsParam, **kwargs) -> dict:
            start_time = time.time()
            ip = request.client.host
            request_params = options.dict() | kwargs
            request_dict = recursive_convert(request_params, rule=_convert_rule)
            query = Query(
                ip=ip,
                identifier=options.identifier,
                method=function.__name__,
                request=request_dict,
                service_id=service_id,
            )
            try:
                result = await function(options=options, **kwargs)
                query.exception = False
                response = create_response(version, exception=False, result=result)
                exception_log = 'OK'
            except Exception as e:
                logger.exception(e)
                query.exception = True
                query.traceback = traceback.format_exc()
                reason = str(e)
                response = create_response(version, exception=True, reason=reason)
                exception_log = f'with exception {reason}'
            query.response = response
            finish_time = time.time()
            query.duration = finish_time - start_time

            db = Database(db_url)
            db.save_query(query)
            logger_method = logger.warning if query.exception else logger.success
            logger_method(f'Query processed in {round(query.duration, 2)}s {exception_log}, {query.method=}')
            return response

        signature = inspect.signature(function)
        parameters = list(signature.parameters.values())
        kind = inspect.Parameter.POSITIONAL_OR_KEYWORD
        parameters.insert(0, inspect.Parameter('request', kind=kind, annotation=Request))

        signature = inspect.Signature(parameters, return_annotation=signature.return_annotation)
        wrapped.__signature__ = signature
        wrapped.__name__ = function.__name__
        return wrapped

    return wrapper


def _convert_rule(value: Any) -> Any:
    if isinstance(value, BaseModel):
        return value.dict()
    return value


def create_response(version: str, exception: bool, **kwargs) -> dict:
    return {
        'version': version,
        'exception': exception,
        **kwargs,
    }
