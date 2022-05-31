from pydantic import BaseModel

from common.services.loader.request.request import ExtractorClass


class TraceServerParam(BaseModel):
    idx: str
    net: str = 'main'
    extractor_class: ExtractorClass = ExtractorClass.TINY
    target: str | None = None
    sort: bool = True
    recognize: bool = True
    highlight: str | None = None
