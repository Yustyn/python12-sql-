import psycopg2
from psycopg2 import Error
from settings import *
import sys


def check_login(login, password):

    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            database='shop_db'
        )
        cursor = connection.cursor()

        data = f"select login, password from login where login like '{login}'"
        cursor.execute(data)
        connection.commit()
        logins_list = cursor.fetchall()
        if logins_list and logins_list[0][1] == password:
            print('You are succesfuly loggined')
        else:
            print('Wrong login or password')
            sys.exit()

    except(Exception, Error) as error:
        print("Error connection: ", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Connection was closed')
