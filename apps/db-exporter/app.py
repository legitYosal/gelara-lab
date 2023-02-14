import mariadb
import sys
import os

try:
    conn = mariadb.connect(
        user=os.environ.get('MARIADB_USER'),
        password=os.environ.get('MARIADB_PASSWORD'),
        host=os.environ.get('MARIADB_HOST'),
        port=os.environ.get('MARIADB_PORT'),
        database=os.environ.get('MARIADB_DATABASE')
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()


