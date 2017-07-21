"""empty message

Revision ID: dc0150516b0b
Revises: 
Create Date: 2017-07-20 12:47:31.242793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc0150516b0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tstresults', sa.Column('test_log', sa.String(length=252), nullable=True))
    op.add_column('tstresults', sa.Column('test_rep', sa.String(length=252), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tstresults', 'test_rep')
    op.drop_column('tstresults', 'test_log')
    # ### end Alembic commands ###