import psycopg2
from bd.config import host, user, password, db_name, port


def get_connect_heroku_bd(zodiac, id):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            port=port
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT {zodiac} FROM goroskop WHERE _id = {id};"""
            )
            text_cursor_bd = cursor.fetchone()
            print(text_cursor_bd[0])
            return text_cursor_bd[0]

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")

if __name__ == "__main__":
    get_connect_heroku_bd(zodiac="Овен", id=id)