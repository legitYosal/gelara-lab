import sys
import os
from time import sleep
from random import randint
import mariadb

if __name__ == '__main__':
    try:
        conn = mariadb.connect(
            user=os.environ.get('MARIADB_USER'),
            password=os.environ.get('MARIADB_PASSWORD'),
            host=os.environ.get('MARIADB_HOST'),
            port=int(os.environ.get('MARIADB_PORT')),
            database=os.environ.get('MARIADB_DATABASE')
        )
    except mariadb.Error as e:
        print(f'Error connecting to MariaDB Platform: {e}')
        sys.exit(1)

    cur = conn.cursor()

    cur.execute('show tables')
    if 'test_table' not in [item[0] for item in cur.fetchall()]:
        cur.execute('create table test_table (name VARCHAR(255))')
        print('created table: test_table')

    sleep(1)
    rand1 = randint(1, 100)
    for i in range(randint(100, 10000)):
        sleep(0.01 + (rand1 / 100)/randint(1,10))
        cur.execute(f'insert into test_table (name) VALUES (?)', ['test' + str(i)]) 
        print(f'Inserted Name: ', 'test' + str(i))
        if randint(1, 100) > 70:
            break
    sleep(10)

    conn.close()
