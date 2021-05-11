"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

import sqlite3

class TemporaryTable:
    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        self.cur.execute('CREATE TABLE points(x int, y int);')

    def __exit__(self, *args):
        print('__exit__ : ', args)
        self.cur.execute('DROP TABLE points;')


def dml(db: str):
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()

        with TemporaryTable(cur):
            cur.execute('INSERT INTO points(x, y) VALUES(1, 1);')
            cur.execute('INSERT INTO points(x, y) VALUES(1, 2);')
            cur.execute('INSERT INTO points(x, y) VALUES(2, 1);')
            cur.execute('INSERT INTO points(x, y) VALUES(2, 2);')

            for row in cur.execute('SELECT x, y FROM points;'):
                print(row)

            for row in cur.execute('SELECT sum(x + y) FROM points;'):
                print(row)

if __name__ == "__main__":
    db = 'test.db'
    dml(db)