from datetime import datetime
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class SourceSchema(BaseModel):
    source_id : int
    source : str(min_length = 200)
    source_type : str(min_length = 20)
    source_tag : str(min_length = 10)
    last_update_date : datetime
    from_date : datetime
    to_date : datetime
    frequencey : str

    class config:
        orm_mode = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    response: Optional[T]