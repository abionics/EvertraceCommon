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
from common.utils.generate_identifier import generate_identifier
from common.utils.recursive_convert import recursive_convert


def endpoint(service_id: int, version: str, db_url: str, accept_options: bool = True):
    def wrapper(function: Callable):
        async def wrapped(request: Request, **kwargs) -> dict:
            ip = request.client.host
            database_params = kwargs.copy()
            request_dict = recursive_convert(database_params, rule=_convert_rule)
            if accept_options:
                options = kwargs.pop('options')
            else:
                identifier = generate_identifier(service_id, ip)
                options = OptionsParam.generate(identifier)
            return await endpoint_actions(function, ip, request_dict, options, service_id, version, db_url, kwargs)

        fix_wrapped_signature(wrapped, function, accept_options)
        return wrapped

    return wrapper


async def endpoint_actions(
        function: Callable,
        ip: str | None,
        request_dict: dict,
        options: OptionsParam,
        service_id: int,
        version: str,
        db_url: str,
        kwargs: dict,
) -> dict:
    start_time = time.time()
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
    db.save(query)
    logger_method = logger.warning if query.exception else logger.success
    logger_method(f'Query processed in {round(query.duration, 2)}s {exception_log}, {query.method=}')
    return response


def fix_wrapped_signature(wrapped: Callable, function: Callable, accept_options: bool):
    signature = inspect.signature(function)
    parameters = list(signature.parameters.values())
    kind = inspect.Parameter.POSITIONAL_OR_KEYWORD
    parameters.insert(0, inspect.Parameter('request', kind=kind, annotation=Request))

    if not accept_options:
        options = next(filter(lambda p: p.name == 'options', parameters))
        parameters.remove(options)

    signature = inspect.Signature(parameters, return_annotation=signature.return_annotation)
    wrapped.__signature__ = signature
    wrapped.__name__ = function.__name__


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
