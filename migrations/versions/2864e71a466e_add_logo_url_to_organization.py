"""Add Logo URL to Organization

Revision ID: 2864e71a466e
Revises: a5abdf9487c
Create Date: 2018-01-25 15:59:31.973635

"""

# revision identifiers, used by Alembic.
revision = '2864e71a466e'
down_revision = 'a5abdf9487c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organization', sa.Column('logo_url', sa.Unicode(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('organization', 'logo_url')
    ### end Alembic commands ###
