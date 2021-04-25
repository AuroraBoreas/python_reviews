# python is protocol orientated lang
# every top-level function has a corresponsing dunder method

# context manager exists everywhere
# with open('04-generator/03_gen.py', 'r') as f:
#     pass


# it works on db as well;

from sqlite3 import connect

# pattern
# __enter__
# __exit__

with connect('text.db') as conn:
    cur = conn.cursor()

    cur.execute('create table points(x int , y int)') # construct, __enter__
    cur.execute('insert into points(x, y) values(1, 1)')
    cur.execute('insert into points(x, y) values(1, 2)')
    cur.execute('insert into points(x, y) values(2, 1)')

    for row in cur.execute('select x, y from points'):
        print(row)

    for row in cur.execute('select sum(x * y) from points'):
        print(row)

    cur.execute('drop table points') # destruct, __exit__
