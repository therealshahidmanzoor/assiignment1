import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('user_details.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table to store user details
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        email TEXT,
        gender TEXT,
        country TEXT,
        occupation TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
