import sqlite3

conn = sqlite3.connect('\project_CSE216\sensor_data.db')
c = conn.cursor()

c.execute("DELETE FROM sensor_data")
conn.commit()
