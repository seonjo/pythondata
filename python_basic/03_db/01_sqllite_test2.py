import sqlite3

conn = sqlite3.connect('python_basic/03_db/example.db')
cur = conn.cursor()

symbol = 'RHAT'
cur.execute('select * from stocks')
data = cur.fetchall()
for item in data:
    print(item)

conn.close()