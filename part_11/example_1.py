import sqlite3

users = [("John", 27, "john@example.com"),
         ("Mike", 22, "mike@example.com")]

conn = sqlite3.connect('example.db')
curs = conn.cursor()
curs.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT NOT NULL, 
                age INTEGER NOT NULL, 
                email TEXT UNIQUE)""")
conn.commit()
curs.execute("""INSERT INTO users (name, age, email) VALUES ("Max", 24, "max24@gmail.com")""")
conn.commit()

curs.executemany("""INSERT INTO users (name, age, email) VALUES (?, ?, ?)""", users)
conn.commit()

curs.execute("""SELECT * FROM users WHERE name = 'Max'""")
rows = curs.fetchall()
for row in rows:
    print(row)
print()
curs.execute("""UPDATE users SET name = 'Oleg' WHERE name = 'Max'""")
conn.commit()
curs.execute("""SELECT * FROM users""")
rows = curs.fetchall()
for row in rows:
    print(row)
print()
curs.execute("""DELETE FROM users WHERE name = 'John'""")
curs.execute("""SELECT * FROM users""")
rows = curs.fetchall()
for row in rows:
    print(row)

curs.close()
