import mariadb
import sys
import os

if __name__ == '__main__':
    try:
        conn = mariadb.connect(
            user=os.environ.get('MARIADB_USER'),
            password=os.environ.get('MARIADB_PASSWORD'),
            host=os.environ.get('MARIADB_HOST'),
            port=os.environ.get('MARIADB_PORT'),
            database=os.environ.get('MARIADB_DATABASE')
        )
    except mariadb.Error as e:
        print(f'Error connecting to MariaDB Platform: {e}')
        sys.exit(1)

    cur = conn.cursor()
    table = 'test_table'

    if table not in cur.execute('show tables'):
        cur.execute('create table test_table (name VARCHAR(255))')
        cur.commit()
        print('created table: ', table)

    cur.execute(f'insert into {table} (name) VALUES (?, ?)', ('test')) 
    cur.commit()
    print(f'Inserted ID: {cur.lastrowid}')

    conn.close()
