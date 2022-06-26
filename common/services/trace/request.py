from pydantic import BaseModel, constr, validator
from pydantic.fields import ModelField
from tvmbase.utils.tvm_utils import is_address, is_idx

from common.services.loader.request.request import ExtractorClass


class TraceServerParam(BaseModel):
    idx: str
    net: constr(strip_whitespace=True) = 'main'
    extractor_class: ExtractorClass = ExtractorClass.TINY
    target: str | None = None
    sort: bool = True
    recognize: bool = True
    highlight: str | None = None

    @validator('idx')
    def idx_validator(cls, value: str) -> str:
        value = value.strip()
        if not is_idx(value):
            raise ValueError(f'"idx" must be an idx, but got "{value}"')
        return value

    @validator('target', 'highlight')
    def address_validator(cls, value: str | None, field: ModelField) -> str | None:
        if value is None:
            return None
        value = value.strip()
        if not is_address(value):
            raise ValueError(f'"{field.name}" must be an address, but got "{value}"')
        return value
