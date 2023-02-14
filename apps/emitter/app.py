import sys
import os
from time import sleep
from random import randint
import mysql.connector
from mysql.connector import Error

if __name__ == '__main__':
    try:
        conn = mysql.connector.connect(
            user=os.environ.get('MARIADB_USER'),
            password=os.environ.get('MARIADB_PASSWORD'),
            host=os.environ.get('MARIADB_HOST'),
            port=int(os.environ.get('MARIADB_PORT')),
            database=os.environ.get('MARIADB_DATABASE')
        )
        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to Server version ", db_Info)
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.execute('show tables')
            if 'test_table' not in [item[0] for item in cursor.fetchall()]:
                cursor.execute('create table test_table (name VARCHAR(255))')
                print('Created table: test_table')

            sleep(1)
            rand1 = randint(1, 100)
            for i in range(randint(100, 10000)):
                sleep(0.01 + (rand1 / 100)/randint(1,10))
                cursor.execute(f'insert into test_table (name) VALUES (%s)', ['test' + str(i)]) 
                print(f'Inserted Name: ', 'test' + str(i))
                if randint(1, 100) > 97:
                    break
            sleep(10)
    except Error as e:
        print("Error while connecting ", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")
