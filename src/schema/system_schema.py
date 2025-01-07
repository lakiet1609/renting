from pydantic import BaseModel, StrictStr
from typing import Optional
from enum import Enum

class StatusEnum(str, Enum):
    success = "success"
    failure = "failure"

class InputModel(BaseModel):
    input_model: StrictStr

class ResultModel(BaseModel):
    output_model: str

class StatusModel(BaseModel):
    status: StatusEnum
    message: Optional[str] = None

class OutputModel(BaseModel):
    result: ResultModel
    status: StatusModel