"""empty message

Revision ID: 34115de1f952
Revises: 8a004f845307
Create Date: 2016-08-04 09:08:40.052294

"""

# revision identifiers, used by Alembic.
revision = '34115de1f952'
down_revision = '8a004f845307'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vul_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('related_vul_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('related_user_email', sa.String(length=64), nullable=True),
    sa.Column('action', sa.String(length=64), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vul_logs')
    ### end Alembic commands ###