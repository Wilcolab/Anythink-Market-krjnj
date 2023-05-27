from sqlalchemy import create_engine
from sqlalchemy.sql import text
import random
import string
import os
env_var = os.environ

# SQLAlchemy >= 1.4 deprecated the use of `postgres://` in favor of `postgresql://`
# for the database connection url
database_url = env_var['DATABASE_URL'].replace("postgres://", "postgresql://")

engine = create_engine(database_url, echo=False)

user_insert_statement = text("""INSERT INTO users(username, email, salt, bio, hashed_password, is_verified) VALUES(:username, :email, :salt, :bio, :hashed_password, :is_verified)""")
select_last_user_id = text("""SELECT * FROM users ORDER BY id DESC LIMIT 1""")
item_statement = text("""INSERT INTO items(slug, title, description, seller_id) VALUES(:slug, :title, :description, :seller_id)""")

letters = string.ascii_lowercase

def create_user_and_item(con, slug, is_verified):
  random_username = ''.join(random.choice(letters) for i in range(10))

  user = {
    'username': random_username,
    'email': f'{random_username}@mail.com',
    'salt': 'abc',
    'bio': 'bio',
    'hashed_password': '12345689',
    'is_verified': is_verified
  }

  con.execute(user_insert_statement, **user)

  result = con.execute(select_last_user_id)

  generated_user_id = None
  for row in result:
    generated_user_id = row['id']

  item = {
    'slug': slug,
    'title': 'title',
    'description': ' description',
    'seller_id': generated_user_id
  }

  con.execute(item_statement, **item)

with engine.connect() as con:
    create_user_and_item(con, 'verified_seller_item', True)
    create_user_and_item(con, 'not_verified_seller_item', False)

