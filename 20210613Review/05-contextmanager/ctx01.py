"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

import sqlite3
import logging
from typing import NewType

logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(message)s')

Path = NewType('Path', str)

def dml(db: Path)->None:
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()

        cur.execute('CREATE TABLE points(x int, y int);')
        cur.execute('INSERT INTO points(x, y) VALUES(1, 1);')
        cur.execute('INSERT INTO points(x, y) VALUES(1, 2);')
        cur.execute('INSERT INTO points(x, y) VALUES(2, 1);')
        cur.execute('INSERT INTO points(x, y) VALUES(2, 2);')
        
        for row in cur.execute('SELECT x, y FROM points;'):
            logging.error(row)

        for row in cur.execute('SELECT sum(x + y) FROM points;'):
            logging.error(row)

        cur.execute('DROP TABLE points;')

if __name__ == "__main__":
    db = 'test.db'
    dml(db)