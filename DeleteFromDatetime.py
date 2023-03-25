import sqlite3
import datetime

# Create a connection to the SQLite database
conn = sqlite3.connect('\project_CSE216\sensor_data.db')

# Create a cursor object
cursor = conn.cursor()

# Create a datetime object
dt = datetime.datetime(2023, 3, 24, 16, 18, 32)

# Convert the datetime object to a string in the format YYYY-MM-DD HH:MM:SS
dt_str = dt.strftime('%Y-%m-%d %H:%M:%S')

# Delete the row with the specified datetime value
cursor.execute("DELETE FROM sensor_data WHERE timestamp = ?", (dt_str,))

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
