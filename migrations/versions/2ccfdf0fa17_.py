"""empty message

Revision ID: 2ccfdf0fa17
Revises: 2dd1855e947
Create Date: 2015-12-15 23:54:46.660838

"""

# revision identifiers, used by Alembic.
revision = '2ccfdf0fa17'
down_revision = '2dd1855e947'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('components',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('line_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Numeric(precision=12, scale=2), nullable=False),
    sa.Column('purchase_order', sa.Integer(), nullable=False),
    sa.Column('component', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['component'], ['components.id'], ),
    sa.ForeignKeyConstraint(['purchase_order'], ['purchase_orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('component')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('component',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('line_items')
    op.drop_table('components')
    ### end Alembic commands ###