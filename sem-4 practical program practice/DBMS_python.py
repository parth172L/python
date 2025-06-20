#database and insert values into it.

import sqlite3
# Connect to (or create) database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Insert data
students_data = [
    ('Alice', 20),
    ('Bob', 22),
    ('Charlie', 19)
]

cursor.executemany('INSERT INTO students (name, age) VALUES (?, ?)', students_data)
conn.commit()

print("Data inserted successfully.")
conn.close()