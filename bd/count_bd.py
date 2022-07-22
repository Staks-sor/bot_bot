import asyncio

import psycopg2

from bd.config import host, user, password, db_name, port


async def get_connect_heroku_bd(zodiac, id):
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


async def get_id(id=21):
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


async def user_reg(name_user, user_id):
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


async def user_examination(user_id):
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


async def tz_reg(oglavlenie, stec, opis):
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


async def tz_search(search):
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


if __name__ == "__main__":
    name = ''
    id_us = ''
    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(get_connect_heroku_bd(zodiac="Овен", id=1)), ioloop.create_task(get_id()),
             ioloop.create_task(get_id_index()), ioloop.create_task(user_reg(name, id_us)),
             ioloop.create_task(user_examination(user_id=user))]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()
