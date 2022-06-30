import os
import psycopg2


DATABASE_URL = os.environ['heroku pg:psql postgresql-pointy-62463 --app botmyffff']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
print(conn)