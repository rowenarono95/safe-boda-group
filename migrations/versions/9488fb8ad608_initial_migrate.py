"""initial migrate

Revision ID: 9488fb8ad608
Revises: 
Create Date: 2020-11-03 21:17:56.208268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9488fb8ad608'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('riders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ridername', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('profile_pic_path', sa.String(), nullable=True),
    sa.Column('pass_secure', sa.String(length=255), nullable=True),
    sa.Column('number_plate', sa.String(length=255), nullable=True),
    sa.Column('motorbike_model', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_riders_email'), 'riders', ['email'], unique=True)
    op.create_index(op.f('ix_riders_number_plate'), 'riders', ['number_plate'], unique=True)
    op.create_index(op.f('ix_riders_ridername'), 'riders', ['ridername'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_riders_ridername'), table_name='riders')
    op.drop_index(op.f('ix_riders_number_plate'), table_name='riders')
    op.drop_index(op.f('ix_riders_email'), table_name='riders')
    op.drop_table('riders')
    # ### end Alembic commands ###
