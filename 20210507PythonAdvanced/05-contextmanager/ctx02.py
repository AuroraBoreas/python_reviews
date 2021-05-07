"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

import sqlite3
import contextlib

@contextlib.contextmanager
def temporary_table(cur):
    cur.execute('CREATE TABLE points(x int, y int);')
    try:
        yield
    finally:
        cur.execute('DROP TABLE points;')

def dml(path: str):
    with sqlite3.connect(path) as conn:
        cur = conn.cursor()

        with temporary_table(cur):
            cur.execute('INSERT INTO points(x, y) VALUES(1, 1);')
            cur.execute('INSERT INTO points(x, y) VALUES(1, 2);')
            cur.execute('INSERT INTO points(x, y) VALUES(2, 1);')
            cur.execute('INSERT INTO points(x, y) VALUES(2, 2);')

            for row in cur.execute('SELECT x,y FROM points;'):
                print(row)

            for row in cur.execute('SELECT sum(x * y) FROM points;'):
                print(row)

if __name__ == '__main__':
    path = 'test.db'
    dml(path)