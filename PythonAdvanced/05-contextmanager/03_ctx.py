# python is a protocol orientated lang
# every top-level function has a corresponding dunder method implemented

from sqlite3 import connect
import contextlib

@contextlib.contextmanager
def temporary_table(cur):
    cur.execute('create table points(x int, y int);')
    try:
        yield
    finally:
        cur.execute('drop table points;')

with connect('text.db') as conn:
    cur = conn.cursor()
    with temporary_table(cur):
        cur.execute('insert into points(x, y) values(1, 1);')
        cur.execute('insert into points(x, y) values(1, 2);')
        cur.execute('insert into points(x, y) values(2, 1);')

        for row in cur.execute('select x, y from points;'):
            print(row)

        for row in cur.execute('select sum(x * y) from points;'):
            print(row)
