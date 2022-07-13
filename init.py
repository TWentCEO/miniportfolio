import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("insert into portfolio values ('김태우', '안녕하세요', 'https://')")
con.commit()
cur.execute("SELECT * FROM portfolio ")
rows = cur.fetchall()
print(rows)
con.close()
