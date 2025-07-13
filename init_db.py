import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# 🚨 DROP the old table
cursor.execute("DROP TABLE IF EXISTS users")

# ✅ Create fresh with password column
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    api_key TEXT UNIQUE NOT NULL
)
""")

conn.commit()
conn.close()

print("Database reset and users table recreated.")

