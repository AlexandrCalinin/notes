from pydantic import BaseModel
from datetime import datetime
from typing import List
from sqlalchemy.dialects.postgresql import UUID

from microservices.notes.schemas.tags import Tag


class NoteBase(BaseModel):
    title: str
    note_body: str


class Note(NoteBase):
    id: UUID
    is_archived: bool
    create_timestamp: datetime
    update_timestamp: datetime
    user_id: UUID
    tags: List[Tag] = []

    class Config:
        orm_mode = True