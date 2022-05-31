from pydantic import BaseModel


class UploadParam(BaseModel):
    hash: str
    abi: str


class CheckParam(BaseModel):
    hash: str
