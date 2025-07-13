import sqlite3

# Connect to your database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Show all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# Show all rows in users table
cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()

print("\nUsers table:")
for row in rows:
    print(row)

conn.close()