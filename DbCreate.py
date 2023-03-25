import sqlite3

# filename to form database
file = '\project_CSE216\sensor_data.db'

try:
    conn = sqlite3.connect(file)
    print("Database Sqlite3.db formed.")
except:
    print("Database Sqlite3.db not formed.")
