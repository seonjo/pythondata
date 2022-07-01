import cx_Oracle

# print(cx_Oracle.version)
conn = cx_Oracle.connect('product/1@localhost:1521/xe')
cur = conn.cursor()
data = (30, 'adfadsffasd', 'USER01')
sql = 'insert into board values(:1,:2,:3,sysdate)'
cur.execute(sql,data)
conn.commit()
sql = 'select * from board'
cur.execute(sql)
data = cur.fetchall()
for item in data:
    print(item)
conn.close()
