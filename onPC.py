from flask import Flask, request, g
import json
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'data.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    gas_concentration = data.get('gas_concentration')
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    db = get_db()
    db.execute('INSERT INTO sensor_data (gas_concentration, temperature, humidity) VALUES (?, ?, ?)',
               [gas_concentration, temperature, humidity])
    db.commit()
    return 'Data received'

if __name__ == '__main__':
    with app.app_context():
        db = get_db()
        db.execute('CREATE TABLE IF NOT EXISTS sensor_data (id INTEGER PRIMARY KEY AUTOINCREMENT, gas_concentration INTEGER, temperature REAL, humidity REAL)')
        db.commit()
    app.run(host='0.0.0.0', port=5000)
