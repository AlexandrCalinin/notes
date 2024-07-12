from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID


class TagBase(BaseModel):
    name: str


class Tag(TagBase):
    id: UUID
    name: str
    create_timestamp: datetime
    update_timestamp: datetime
    note_id: UUID

    class Config:
        orm_mode = True
