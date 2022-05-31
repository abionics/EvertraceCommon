from pydantic import BaseModel


class UploadParam(BaseModel):
    name: str
    hash: str
    abi: str


class CheckParam(BaseModel):
    hash: str


class LoadParam(BaseModel):
    hashes: list[str]
    ignore_not_found: bool = False
