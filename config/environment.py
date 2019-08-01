import os

db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/radiohead')
secret = os.getenv('SECRET', 'my secret')
