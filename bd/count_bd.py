import psycopg2
from psycopg2._psycopg import connection

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


# def get_id():
#     try:
#         connection = psycopg2.connect(
#             host=host,
#             user=user,
#             password=password,
#             database=db_name,
#             port=port
#         )
#         connection.autocommit = True
#
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 """INSERT INTO bot_id (id) VALUES
#                 (5);"""
#             )
#
#             print("[INFO] Data was succefully inserted")
#
#     except Exception as _ex:
#         print("[INFO] Error while working with PostgreSQL", _ex)
#     finally:
#         if connection:
#             # cursor.close()
#             connection.close()
#             print("[INFO] PostgreSQL connection closed")
#
#
#
#
# def get_id_index():
#     try:
#         connection = psycopg2.connect(
#             host=host,
#             user=user,
#             password=password,
#             database=db_name,
#             port=port
#         )
#         connection.autocommit = True
#
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 f"""SELECT * FROM bot_id WHERE id = 1;"""
#             )
#             text_cursor_bd = cursor.fetchone()
#             print(text_cursor_bd[0])
#             return text_cursor_bd[0]
#
#     except Exception as _ex:
#         print("[INFO] Error while working with PostgreSQL", _ex)
#     finally:
#         if connection:
#             # cursor.close()
#             connection.close()
#             print("[INFO] PostgreSQL connection closed")


if __name__ == "__main__":
    get_connect_heroku_bd(zodiac="Овен", id=1)
    # get_id()
    # get_id_index()