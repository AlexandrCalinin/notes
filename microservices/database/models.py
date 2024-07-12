from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, ForeignKey, String, Boolean, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}

    id = Column("id", UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    first_name = Column("first_name", String(100), nullable=False)
    last_name = Column("last_name", String(100), nullable=False)
    create_timestamp = Column("create_timestamp", DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_timestamp = Column("update_timestamp", DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    email = Column("email", String(100), unique=True, nullable=False)


class Notes(Base):
    __tablename__ = "notes"
    __table_args__ = {"schema": "notes"}

    id = Column("id", UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    title = Column("title", String(64), nullable=False)
    note_body = Column("body", String(512), nullable=False)
    is_archived = Column("is_archived", Boolean, default=False)
    create_timestamp = Column("create_timestamp", DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_timestamp = Column("update_timestamp", DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    user_id = Column("user", UUID(as_uuid=True), ForeignKey("auth.users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User")
    tags = relationship("Tags", back_populates="notes")


class Tags(Base):
    __tablename__ = "tags"
    __table_args__ = {"schema": "notes"}

    id = Column("id", UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    name = Column("name", String(50), nullable=False)
    create_timestamp = Column("create_timestamp", DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_timestamp = Column("update_timestamp", DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    note_id = Column("note", UUID(as_uuid=True), ForeignKey("notes.notes.id", ondelete="CASCADE"), nullable=False)
    note = relationship("Notes", back_populates="tags")