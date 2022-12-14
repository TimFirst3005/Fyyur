"""Initial migration.

Revision ID: 4e4bf3f972cd
Revises: 
Create Date: 2022-11-11 01:50:26.905206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e4bf3f972cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('show')
    op.add_column('artists', sa.Column('website', sa.String(length=120), nullable=True))
    op.alter_column('artists', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('artists', 'website_link')
    op.add_column('venues', sa.Column('website', sa.String(length=120), nullable=True))
    op.drop_column('venues', 'website_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('website_link', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('venues', 'website')
    op.add_column('artists', sa.Column('website_link', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.alter_column('artists', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('artists', 'website')
    op.create_table('show',
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], name='show_artist_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], name='show_venue_id_fkey'),
    sa.PrimaryKeyConstraint('venue_id', 'artist_id', name='show_pkey')
    )
    op.drop_table('shows')
    # ### end Alembic commands ###
