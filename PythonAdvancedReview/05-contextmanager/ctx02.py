"# Python is a protocol orientated lang; \n# every top-level function has a corresponding dunder method implemented;" 

import contextlib
import sqlite3

"""

[ contextlib ]
===
* why?
A: it is basically the same thing;
but it is simple, quick, and stupid to write

* note:
A: __enter__
__exit__

===

"""

@contextlib.contextmanager
def temporary_table(cur):
    # __enter__
    cur.execute("CREATE TABLE points(x int, y int);")
    try:
        yield
    finally:
        # __exit__
        cur.execute('DROP TABLE points;')


with sqlite3.connect('test.db') as conn:
    cur = conn.cursor()
    with temporary_table(cur):
        cur.execute("INSERT INTO points(x, y) values(1, 1);")
        cur.execute("INSERT INTO points(x, y) values(1, 2);")
        cur.execute("INSERT INTO points(x, y) values(2, 1);")

        for row in cur.execute("SELECT x, y FROM points;"):
            print(row)

        for row in cur.execute("SELECT sum(x*y) FROM points;"):
            print(row)