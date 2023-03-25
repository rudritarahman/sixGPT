import sqlite3

conn = sqlite3.connect('\project_CSE216\sensor_data.db')
c = conn.cursor()

c.execute('''CREATE TABLE sensor_data
             (timestamp TEXT, temperature REAL, humidity REAL, methane REAL)''')

conn.commit()
conn.close()
