# python is a protocol orientated lang
# every top-level function has a corresponding dunder method implemented

# using __enter__ and __exit__ pair to create a class
# to implement "resource allocation is initialization" concept in C++

from sqlite3.dbapi2 import connect

# sequencing
def temporary_table(cur):
    print('__enter__')
    cur.execute('create table points(x int, y int);')
    yield
    print('__exit__')
    cur.execute('drop table points;')

class TemporaryTable:
    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        self.gen = temporary_table(self.cur)
        next(self.gen)

    def __exit__(self, *args):
        next(self.gen, None)

with connect('text.db') as conn:
    cur = conn.cursor()
    with TemporaryTable(cur):
        cur.execute('insert into points(x, y) values(1, 1);')
        cur.execute('insert into points(x, y) values(1, 2);')
        cur.execute('insert into points(x, y) values(2, 1);')

        for row in cur.execute('select x, y from points;'):
            print(row)

        for row in cur.execute('select sum(x * y) from points;'):
            print(row)
