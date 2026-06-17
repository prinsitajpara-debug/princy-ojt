# """create tags table

# Revision ID: 6a71b0f42c22
# Revises: 5d24414903f4
# Create Date: 2026-06-16 15:19:08.631592

# """
# from typing import Sequence, Union

# from alembic import op
# import sqlalchemy as sa


# # revision identifiers, used by Alembic.
# revision: str = '6a71b0f42c22'
# down_revision: Union[str, Sequence[str], None] = '5d24414903f4'
# branch_labels: Union[str, Sequence[str], None] = None
# depends_on: Union[str, Sequence[str], None] = None


# def upgrade() -> None:
#     """Upgrade schema."""
#     pass


# def downgrade() -> None:
#     """Downgrade schema."""
#     pass
"""create tags table

Revision ID: 6a71b0f42c22
Revises: 5d24414903f4
Create Date: 2026-06-16 15:19:08.631592

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "6a71b0f42c22"
down_revision: Union[str, Sequence[str], None] = "5d24414903f4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tags",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(50))
    )


def downgrade() -> None:
    op.drop_table("tags")