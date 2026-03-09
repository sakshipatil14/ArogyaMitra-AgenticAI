import sqlite3

conn = sqlite3.connect("arogyamitra.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
weight REAL,
goal TEXT,
workout_time INTEGER,
diet TEXT
)
""")

conn.commit()
conn.close()

print("Database and table created successfully")