import sqlite3 as lite

con = lite.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchall()[0]
    print(f'SQLite version: {data}')

    try:
        cur.execute("create table cars(id int, name text, price int)")
    except lite.OperationalError as e:
        print(e)

    cur.execute("insert into cars values(1, 'Audi', 52642)")
    cur.execute("insert into cars values(2, 'Opel', 20000)")
    cur.execute("insert into cars values(3, 'Skoda', 9000)")

    cur.execute("select * from cars")

    for row in cur.fetchall():
        print(row)
