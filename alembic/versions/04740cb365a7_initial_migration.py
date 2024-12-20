"""Initial migration

Revision ID: 04740cb365a7
Revises: 
Create Date: 2024-12-19 14:57:15.413185
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '04740cb365a7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto-generated by Alembic - please adjust! ###
    # op.drop_table('borrowed_books')  # Remove this line since the table doesn't exist
    # op.drop_table('borrowers')
    # op.drop_table('authors')
    # op.drop_table('books')
    # ### end Alembic commands ###

    # Add any other operations that you need to perform here

  def downgrade() -> None:
    # ### commands auto-generated by Alembic - please adjust! ###
    op.create_table('books',
        sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('title', mysql.VARCHAR(length=255), nullable=False),
        sa.Column('author_id', mysql.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(['author_id'], ['authors.id'], name='books_ibfk_1'),
        sa.PrimaryKeyConstraint('id'),
        mysql_collate='utf8mb4_0900_ai_ci',
        mysql_default_charset='utf8mb4',
        mysql_engine='InnoDB'
    )
    op.create_table('authors',
        sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        mysql_collate='utf8mb4_0900_ai_ci',
        mysql_default_charset='utf8mb4',
        mysql_engine='InnoDB'
    )
    op.create_table('borrowers',
        sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
        sa.Column('email', mysql.VARCHAR(length=255), nullable=False),
        sa.Column('phone', mysql.VARCHAR(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        mysql_collate='utf8mb4_0900_ai_ci',
        mysql_default_charset='utf8mb4',
        mysql_engine='InnoDB'
    )
    op.create_table('borrowed_books',
        sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('book_id', mysql.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('borrower_id', mysql.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('borrow_date', sa.DATE(), nullable=True),
        sa.Column('return_date', sa.DATE(), nullable=True),
        sa.ForeignKeyConstraint(['book_id'], ['books.id'], name='borrowed_books_ibfk_1'),
        sa.ForeignKeyConstraint(['borrower_id'], ['borrowers.id'], name='borrowed_books_ibfk_2'),
        sa.PrimaryKeyConstraint('id'),
        mysql_collate='utf8mb4_0900_ai_ci',
        mysql_default_charset='utf8mb4',
        mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
