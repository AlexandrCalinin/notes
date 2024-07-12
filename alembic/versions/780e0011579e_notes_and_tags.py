"""notes_and_tags

Revision ID: 780e0011579e
Revises: 41a01d630d3e
Create Date: 2024-07-12 07:48:14.938693

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "780e0011579e"
down_revision: Union[str, None] = "41a01d630d3e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS notes;")

    op.create_table(
        "notes",
        sa.Column("id", postgresql.UUID, primary_key=True, server_default=sa.text("uuid_generate_v4()")),
        sa.Column("title", sa.String(64), nullable=False),
        sa.Column("note_body", sa.String(512), nullable=False),
        sa.Column("is_archived", sa.Boolean, default=False),
        sa.Column("create_timestamp", sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("update_timestamp", sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("user_id", postgresql.UUID, sa.ForeignKey("auth.users.id", ondelete="CASCADE"), nullable=False),
        schema="notes"
    )

    op.create_table(
        "tags",
        sa.Column("id", postgresql.UUID, primary_key=True, server_default=sa.text("uuid_generate_v4()")),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("create_timestamp", sa.DateTime, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column("update_timestamp", sa.DateTime, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column("note_id", postgresql.UUID, nullable=False),
        sa.ForeignKeyConstraint(['note_id'], ['notes.notes.id'], ondelete='CASCADE'),
        schema="notes"
    )


def downgrade() -> None:
    op.drop_table("tags", schema="notes")
    op.drop_table("notes", schema="notes")
    op.execute("DROP SCHEMA IF EXISTS notes CASCADE;")

