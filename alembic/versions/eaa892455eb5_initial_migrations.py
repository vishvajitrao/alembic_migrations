"""Initial migrations

Revision ID: eaa892455eb5
Revises: 
Create Date: 2021-12-16 16:04:17.743628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eaa892455eb5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authentication',
    sa.Column('id', sa.String(length=40), nullable=False),
    sa.Column('access_token', sa.String(length=1500), nullable=False),
    sa.Column('expires_in', sa.String(length=10), nullable=False),
    sa.Column('refresh_expires_in', sa.String(length=20), nullable=False),
    sa.Column('refresh_token', sa.String(length=700), nullable=False),
    sa.Column('token_type', sa.String(length=50), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('call_notes',
    sa.Column('id', sa.String(length=40), nullable=False),
    sa.Column('user_phone', sa.String(length=20), nullable=False),
    sa.Column('note', sa.String(), nullable=False),
    sa.Column('account_id', sa.String(), nullable=True),
    sa.Column('card_id', sa.String(), nullable=True),
    sa.Column('bag_id', sa.String(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('created_by', sa.String(length=40), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('created_on_timestamp', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('call_notes')
    op.drop_table('authentication')
    # ### end Alembic commands ###
