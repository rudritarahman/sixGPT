import sqlite3

conn = sqlite3.connect('\project_CSE216\sensor_data.db')
c = conn.cursor()

i = 0
while i < 1:
    c.execute("INSERT INTO sensor_data (timestamp , temperature , humidity , methane) VALUES (datetime('now','localtime'), ?, ?,?)",
              (22, 75, 1300))
    conn.commit()
    i = i+1
