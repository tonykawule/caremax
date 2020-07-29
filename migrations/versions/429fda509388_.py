"""empty message

Revision ID: 429fda509388
Revises: 
Create Date: 2020-06-20 23:51:44.439363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '429fda509388'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('families', sa.Column('contact', sa.String(length=15), nullable=False))
    op.drop_column('families', 'contactphone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('families', sa.Column('contactphone', sa.VARCHAR(length=15), autoincrement=False, nullable=False))
    op.drop_column('families', 'contact')
    # ### end Alembic commands ###
