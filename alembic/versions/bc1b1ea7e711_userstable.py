"""UsersTable

Revision ID: bc1b1ea7e711
Revises: db70140f9c2e
Create Date: 2021-05-13 15:58:13.086932

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bc1b1ea7e711'
down_revision = 'db70140f9c2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('row_id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('row_created', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('row_updated', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('wallet_address', sa.VARCHAR(length=50), nullable=False),
    sa.Column('signature', sa.VARCHAR(length=255), nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), nullable=True),
    sa.Column('is_registered', mysql.BIT(), nullable=True),
    sa.PrimaryKeyConstraint('row_id'),
    sa.UniqueConstraint('wallet_address')
    )
    op.alter_column('transfer_info', 'is_contract',
               existing_type=mysql.BIT(length=1),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('transfer_info', 'is_contract',
               existing_type=mysql.BIT(length=1),
               nullable=False)
    op.drop_table('users')
    # ### end Alembic commands ###
