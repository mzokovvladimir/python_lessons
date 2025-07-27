import sqlite3

conn = sqlite3.connect("relations.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

# (1:M)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount REAL NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
""")
conn.commit()

cursor.execute("INSERT INTO users (name) VALUES (?)", ("Іван",))
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Ольга",))
conn.commit()

cursor.execute("SELECT id FROM users WHERE name = 'Іван'")
ivan_id = cursor.fetchone()[0]

cursor.execute("INSERT INTO orders (user_id, amount, date) VALUES (?, ?, ?)", (ivan_id, 250.5, "2024-02-14"))
cursor.execute("INSERT INTO orders (user_id, amount, date) VALUES (?, ?, ?)", (ivan_id, 130.0, "2024-02-15"))
conn.commit()

cursor.execute("""
    SELECT orders.id, users.name, orders.amount, orders.date
    FROM orders
    JOIN users ON orders.user_id = users.id
""")
print(cursor.fetchall())


# (M:M)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_courses (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
        FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
    )
""")
conn.commit()


cursor.executemany("INSERT INTO students (name) VALUES (?)", [("Андрій",), ("Марина",)])
cursor.executemany("INSERT INTO courses (title) VALUES (?)", [("Python",), ("Machine Learning",)])
conn.commit()

cursor.execute("SELECT id FROM students WHERE name = 'Андрій'")
andriy_id = cursor.fetchone()[0]

cursor.execute("SELECT id FROM courses WHERE title = 'Python'")
python_id = cursor.fetchone()[0]

cursor.execute("INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)", (andriy_id, python_id))
conn.commit()


cursor.execute("""
    SELECT students.name, courses.title 
    FROM student_courses
    JOIN students ON student_courses.student_id = students.id
    JOIN courses ON student_courses.course_id = courses.id
""")
print(cursor.fetchall())


# (1:1)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        phone TEXT,
        address TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
""")
conn.commit()

cursor.execute("SELECT id FROM users WHERE name = 'Ольга'")
olga_id = cursor.fetchone()[0]

cursor.execute("INSERT INTO profiles (user_id, phone, address) VALUES (?, ?, ?)", (olga_id, "+380501234567", "Київ"))
conn.commit()

cursor.execute("""
    SELECT users.name, profiles.phone, profiles.address 
    FROM users
    LEFT JOIN profiles ON users.id = profiles.user_id
""")
print(cursor.fetchall())
