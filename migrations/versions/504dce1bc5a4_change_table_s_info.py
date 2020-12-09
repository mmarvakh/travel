"""Change table's info

Revision ID: 504dce1bc5a4
Revises: b81b8125d893
Create Date: 2020-12-09 13:06:00.411942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '504dce1bc5a4'
down_revision = 'b81b8125d893'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Hotel_reviews',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.VARCHAR(length=1000), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['Clients.id'], ),
    sa.ForeignKeyConstraint(['hotel_id'], ['Hotels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Request_vouchers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tour_request_id', sa.Integer(), nullable=False),
    sa.Column('client_contract_id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('voucher', sa.VARCHAR(length=255), nullable=False),
    sa.ForeignKeyConstraint(['client_contract_id'], ['Clients_contracts.id'], ),
    sa.ForeignKeyConstraint(['service_id'], ['Services.id'], ),
    sa.ForeignKeyConstraint(['tour_request_id'], ['Tour_requests.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Vouchers')
    op.drop_table('Reviews')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Reviews',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Reviews_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('content', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
    sa.Column('hotel_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('client_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['Clients.id'], name='Reviews_client_id_fkey'),
    sa.ForeignKeyConstraint(['hotel_id'], ['Hotels.id'], name='Reviews_hotel_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Reviews_pkey')
    )
    op.create_table('Vouchers',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Vouchers_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('voucher', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('tour_request_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('client_contract_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('service_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['client_contract_id'], ['Clients_contracts.id'], name='Vouchers_client_contract_id_fkey'),
    sa.ForeignKeyConstraint(['service_id'], ['Services.id'], name='Vouchers_service_id_fkey'),
    sa.ForeignKeyConstraint(['tour_request_id'], ['Tour_requests.id'], name='Vouchers_tour_request_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Vouchers_pkey')
    )
    op.drop_table('Request_vouchers')
    op.drop_table('Hotel_reviews')
    # ### end Alembic commands ###
