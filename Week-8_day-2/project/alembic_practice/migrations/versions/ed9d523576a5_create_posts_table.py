# """create posts table

# Revision ID: ed9d523576a5
# Revises: ff6efd794a34
# Create Date: 2026-06-16 15:15:15.462527

# """
# from typing import Sequence, Union

# from alembic import op
# import sqlalchemy as sa


# # revision identifiers, used by Alembic.
# revision: str = 'ed9d523576a5'
# down_revision: Union[str, Sequence[str], None] = 'ff6efd794a34'
# branch_labels: Union[str, Sequence[str], None] = None
# depends_on: Union[str, Sequence[str], None] = None


# def upgrade() -> None:
#     """Upgrade schema."""
#     pass


# def downgrade() -> None:
#     """Downgrade schema."""
#     pass

"""create posts table

Revision ID: ed9d523576a5
Revises: ff6efd794a34
Create Date: 2026-06-16 15:15:15.462527

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "ed9d523576a5"
down_revision: Union[str, Sequence[str], None] = "ff6efd794a34"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.String(255)),
        sa.Column("content", sa.Text()),
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id")
        )
    )


def downgrade() -> None:
    op.drop_table("posts")