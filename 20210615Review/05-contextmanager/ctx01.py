"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

import sqlite3
from typing import NewType

Path = NewType('Path', str)

def dml(db: Path):
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()

        cur.execute('CREATE TABLE points(x int, y int);')
        cur.execute('INSERT INTO points(x, y) VALUES(1, 1);')
        cur.execute('INSERT INTO points(x, y) VALUES(1, 2);')
        cur.execute('INSERT INTO points(x, y) VALUES(2, 1);')
        cur.execute('INSERT INTO points(x, y) VALUES(2, 2);')

        for row in cur.execute('SELECT x, y FROM points;'):
            print(row)

        for row in cur.execute('SELECT sum(x + y) FROM points;'):
            print(row)

        cur.execute('DROP TABLE points;')

if __name__ == "__main__":
    db = 'test.db'
    dml(db)