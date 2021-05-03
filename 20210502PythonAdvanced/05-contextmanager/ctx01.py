"#python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented" 

import sqlite3

with sqlite3.connect('test.db') as conn:
    cur = conn.cursor()

    # create table
    cur.execute('CREATE TABLE points(x int, y int);')
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
        
    # drop table
    cur.execute('DROP TABLE points;')