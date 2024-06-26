"""initial

Revision ID: b61623f1e263
Revises: 
Create Date: 2024-03-06 13:30:57.708360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'b61623f1e263'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stay',
    sa.Column('location', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('accomodation', sa.Enum('hotel', 'hostel', 'apartments', 'couchsurfing', 'tent', name='accomodationtype'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transition',
    sa.Column('location_from', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('location_to', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('transport', sa.Enum('plane', 'train', 'ship', 'ferry', 'bus', 'car', 'motorbike', 'bycicle', 'walking', 'hitchhiking', name='transporttype'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trip',
    sa.Column('status', sa.Enum('open', 'closed', 'cancelled', name='statustype'), nullable=False),
    sa.Column('member_capacity', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('last_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('gender', sa.Enum('undefined', 'female', 'male', name='gendertype'), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('telephone', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('bio', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('registered', sa.DateTime(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('step',
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('date_from', sa.DateTime(), nullable=False),
    sa.Column('date_to', sa.DateTime(), nullable=False),
    sa.Column('est_price', sa.Float(), nullable=False),
    sa.Column('stay_id', sa.Integer(), nullable=True),
    sa.Column('transition_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['stay_id'], ['stay.id'], ),
    sa.ForeignKeyConstraint(['transition_id'], ['transition.id'], ),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usertriplink',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('role', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('trip_id', 'user_id', name='unique pair of ids')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usertriplink')
    op.drop_table('step')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    op.drop_table('trip')
    op.drop_table('transition')
    op.drop_table('stay')
    # ### end Alembic commands ###
