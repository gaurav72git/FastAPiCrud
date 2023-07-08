from datetime import datetime
from typing import Generic, TypeVar, Optional, List
import uuid
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class SourceSchema(BaseModel):
    source_id : uuid.UUID
    source : str
    source_type : str
    source_tag : str
    last_update_date : datetime
    from_date : datetime
    to_date : datetime
    frequencey : str

    class config:
        orm_mode = True

class ListSources(BaseModel):
    status: str
    results: int
    sources: List[SourceSchema]

class SourceCreatedResponse(SourceSchema):
    pass


class UpdatedSourceResponse(SourceSchema):
    pass