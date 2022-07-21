import psycopg2
from psycopg2._psycopg import connection
import asyncio
from bd.config import host, user, password, db_name, port
from datetime import datetime


def get_connect_heroku_bd(zodiac, id):
    global connection
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
                f"""SELECT {zodiac} FROM gor WHERE _id = {id};"""
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


def get_id(id=8):
    global connection
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
                f"""UPDATE bot_id SET id = {id};"""
            )

            print("[INFO] Data was succefully inserted")

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


def get_id_index():
    global connection
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
                f"""SELECT * FROM bot_id;"""
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


def user_reg(name_user, user_id):
    global connection
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
                f"""INSERT INTO user_bot (name_user, user_id)
                 VALUES('{name_user}', {user_id});"""
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


def user_examination(user_id):
    global connection
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
                f"""SELECT * FROM user_bot WHERE user_id = {user_id};"""
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


def tz_reg(oglavlenie, stec, opis):
    global connection
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
                f"""INSERT INTO tz_bot (ogl, stek, opis)
                 VALUES('{oglavlenie}', '{stec}', '{opis}');"""
            )
            print("[INFO] запись выполнена PostgreSQL")

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")

def tz_search(search):
    global connection
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
                f"""SELECT * FROM tz_bot WHERE stek LIKE '%{search}%';"""
            )
            print("[INFO] поиск выполнен PostgreSQL")

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")

def main():
    name = ""
    id_us = ''
    get_connect_heroku_bd(zodiac="Овен", id=1)
    get_id()
    get_id_index()
    user_reg(name, id_us)
    user_examination(user_id=user)


if __name__ == "__main__":
    main()
