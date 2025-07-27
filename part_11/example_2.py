import sqlite3


try:
    with sqlite3.connect('example.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO users (name, age, email) VALUES ('Roman', 21, 'max24@gmail.com')""")
        connection.commit()

except sqlite3.IntegrityError as error:
    print(f"Error: {error}")