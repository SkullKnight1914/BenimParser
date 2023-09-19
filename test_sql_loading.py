import psycopg2
from config import host, user, password, db_name
import os
import json


try:
    #   connect with exist DB
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT version();"""
        )

        print(f"Server version: {cursor.fetchone()}")

    # for jsObj in os.listdir(r'C:\Users\bulat\PycharmProjects\PA\HHru_parsing\docs\vacancies'):
    #
    #     with open(rf'C:\Users\bulat\PycharmProjects\PA\HHru_parsing\docs\vacancies\{jsObj}', encoding='utf-8') as file:
    #         src = file.read()
    #         src = json.loads(src)

    #   create a new table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE info_about_vac(
                id serial PRIMARY KEY,
                name varchar(75) NOT NULL,
                address varchar(75),
                metro varchar(30),
                experience varchar(30) NOT NULL,
                schedule varchar(30) NOT NULL,
                employment varchar(30) NOT NULL,
                salary_from INT,
                salary_to INT,
                url varchar(50) NOT NULL);"""
        )

        # connection.commit()
        print("[INFO] Table created successfully")


except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print('[INFO] PostgreSQL connection closed')