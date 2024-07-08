"""created new attribute in Question

Revision ID: 80bae91d31bf
Revises: 
Create Date: 2024-07-07 21:30:17.010015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '80bae91d31bf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'questions',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('question', sa.Text, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )

    # Create answers table
    op.create_table(
        'answers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('question_id', sa.Integer, sa.ForeignKey('questions.id', ondelete='CASCADE')),
        sa.Column('answer', sa.Text, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )



def downgrade() -> None:
    op.drop_table('answers')
    # Drop questions table
    op.drop_table('questions')
