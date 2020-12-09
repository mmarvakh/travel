"""Added new FK

Revision ID: b81b8125d893
Revises: 581dddd6bf4a
Create Date: 2020-12-09 12:48:08.031689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b81b8125d893'
down_revision = '581dddd6bf4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Partners_contracts', sa.Column('partner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'Partners_contracts', 'Partners', ['partner_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Partners_contracts', type_='foreignkey')
    op.drop_column('Partners_contracts', 'partner_id')
    # ### end Alembic commands ###
