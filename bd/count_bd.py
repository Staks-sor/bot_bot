import asyncio

import psycopg2

from bd.config import host, user, password, db_name, port
import re


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


async def get_id(id=30):
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


async def tz_reg(title, description, tech_stack, id_user):
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
                f"""INSERT INTO tz_bot (title, description, tech_stack, id_user)
                 VALUES('{title}', '{description}', '{tech_stack}', {id_user});"""
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
                f"""SELECT * FROM tz_bot WHERE tech_stack ~~* '%{search}%';"""
            )
            print("[INFO] поиск выполнен PostgreSQL")
            text_cursor_bd = cursor.fetchall()
            print(text_cursor_bd)

            return text_cursor_bd
    # Обрати внимание на доработку метода вывода^
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


async def tz_examination(id_user):
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
                f"""SELECT COUNT(*) as count FROM tz_bot WHERE id_user={id_user};"""
            )

            text_cursor_bd = cursor.fetchone()
            print(text_cursor_bd)
            return text_cursor_bd

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


async def get_delete_tz(user_id):
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
                f"""DELETE FROM tz_bot
                    WHERE id_user={user_id};"""
            )

            print("[INFO] Data was succefully inserted")

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


async def tz_tz(id_user):
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
                f"""SELECT * FROM tz_bot WHERE id_user={id_user};"""

            )

            text_cursor_bd = cursor.fetchone()
            # print(text_cursor_bd)
            return text_cursor_bd[4]

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


async def otklick_create(create_user_id, user_id):
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
                f"""INSERT INTO otklic_bot (user_create_id, user_id)
                 VALUES('{create_user_id}', {user_id});"""
            )

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


async def get_otklic(search_create, search_id):
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
                # f"""SELECT * FROM otklic_bot WHERE user_create_id  = {search_create};"""
                f"""SELECT * FROM otklic_bot WHERE user_id = {search_id}
                 AND user_create_id  = {search_create};"""

            )

            text_cursor_bd = cursor.fetchone()

            return text_cursor_bd

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")

async def vacant_update(search):
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
                f"""SELECT * FROM tz_bot WHERE id_user = {search};"""
            )
            print("[INFO] поиск выполнен PostgreSQL")
            text_cursor_bd = cursor.fetchone()
            print(text_cursor_bd)

            return text_cursor_bd
    # Обрати внимание на доработку метода вывода^
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")





if __name__ == "__main__":
    pass
    # name = ''
    # id_us = ''
    # ioloop = asyncio.get_event_loop()
    # tasks = [ioloop.create_task(get_connect_heroku_bd(zodiac="Овен", id=1)), ioloop.create_task(get_id()),
    #          ioloop.create_task(get_id_index()), ioloop.create_task(user_reg(name, id_us)),
    #          ioloop.create_task(user_examination(user_id=user)), ioloop.create_task(tz_search(search='steck')),
    #          ioloop.create_task(get_delete_tz(user_id=user))]
    # wait_tasks = asyncio.wait(tasks)
    # ioloop.run_until_complete(wait_tasks)
    # ioloop.close()
