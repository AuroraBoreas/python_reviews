"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

import sqlite3
from typing import NewType, Any
Path   = NewType('Path', str)
Cursor = NewType('Cursor', sqlite3.Cursor)

class TemporaryTable:
    def __init__(self, cur:Cursor):
        self.cur = cur

    def __enter__(self):
        self.cur.execute('CREATE TABLE points(x int, y int);')

    def __exit__(self, *args:Any):
        print('__exit__ : ', args)
        self.cur.execute('DROP TABLE points;')

def dml(db:Path)->None:
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()

        with TemporaryTable(cur):
            cur.execute('INSERT INTO points(x, y) VALUES(1, 1);')
            cur.execute('INSERT INTO points(x, y) VALUES(1, 2);')
            cur.execute('INSERT INTO points(x, y) VALUES(2, 1);')
            cur.execute('INSERT INTO points(x, y) VALUES(2, 2);')

            for row in cur.execute('SELECT x, y FROM points;'):
                print(row)

            for row in cur.execute('SELECT SUM(x + y) FROM points;'):
                print(row)

if __name__ == '__main__':
    db = 'test.db'
    dml(db)