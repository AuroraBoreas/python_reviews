"# Python is a protocol orientated lang; \n# every top-level function has a corresponding dunder method implemented;" 

"""

[ contextmanager ]
===
* what?
A: "resource management is initialization" in C++;
with statement in python;

===


"""

import sqlite3

with sqlite3.connect('test.db') as conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE points(x int, y, int);')
    cur.execute('INSERT INTO points(x, y) values(1, 1);')
    cur.execute('INSERT INTO points(x, y) values(1, 2);')
    cur.execute('INSERT INTO points(x, y) values(2, 1);')

    for row in cur.execute('SELECT x, y FROM points;'):
        print(row)
    
    for row in cur.execute('SELECT sum(x*y) FROM points;'):
        print(row)

    cur.execute('DROP TABLE points;')