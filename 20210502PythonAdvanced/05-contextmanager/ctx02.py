"#python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented" 

import sqlite3
import contextlib

@contextlib.contextmanager
def temporary_table(cur):
    # create
    cur.execute('CREATE TABLE points(x int, y int);')
    try:
        yield
    finally:
        # drop
        cur.execute('DROP TABLE points;')

with sqlite3.connect('test.db') as conn:
    cur = conn.cursor()

    with temporary_table(cur):
        # insert into
        cur.execute('INSERT INTO points(x, y) VALUES(1, 1);')
        cur.execute('INSERT INTO points(x, y) VALUES(1, 2);')
        cur.execute('INSERT INTO points(x, y) VALUES(2, 1);')
        cur.execute('INSERT INTO points(x, y) VALUES(2, 2);')
        # SELECT
        for row in cur.execute('SELECT x, y from points;'):
            print(row)
        
        for row in cur.execute('SELECT sum(x * y) from points;'):
            print(row)
                    
