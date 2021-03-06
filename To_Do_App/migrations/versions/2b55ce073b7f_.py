"""empty message

Revision ID: 2b55ce073b7f
Revises: 61a2854387b8
Create Date: 2020-06-13 13:56:20.461102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b55ce073b7f'
down_revision = '61a2854387b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'todos', 'todolists', ['list_id'], ['id'])
   # op.execute('update todos set list_id = 1 where list_id is NULL;')
   # op.alter_column('todos', 'list_id', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'list_id')
    op.drop_table('todolists')
    # ### end Alembic commands ###
