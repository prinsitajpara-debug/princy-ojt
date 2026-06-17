# """create comments table

# Revision ID: 5d24414903f4
# Revises: ed9d523576a5
# Create Date: 2026-06-16 15:18:48.343509

# """
# from typing import Sequence, Union

# from alembic import op
# import sqlalchemy as sa


# # revision identifiers, used by Alembic.
# revision: str = '5d24414903f4'
# down_revision: Union[str, Sequence[str], None] = 'ed9d523576a5'
# branch_labels: Union[str, Sequence[str], None] = None
# depends_on: Union[str, Sequence[str], None] = None


# def upgrade() -> None:
#     """Upgrade schema."""
#     pass


# def downgrade() -> None:
#     """Downgrade schema."""
#     pass
"""create comments table

Revision ID: 5d24414903f4
Revises: ed9d523576a5
Create Date: 2026-06-16 15:18:48.343509

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "5d24414903f4"
down_revision: Union[str, Sequence[str], None] = "ed9d523576a5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "comments",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("text", sa.Text()),
        sa.Column(
            "post_id",
            sa.Integer(),
            sa.ForeignKey("posts.id")
        ),
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id")
        )
    )


def downgrade() -> None:
    op.drop_table("comments")