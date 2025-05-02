from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

# Путь к файлу базы данных (монтируется через docker-compose)
DB_PATH = '/data/database.db'

@app.route('/users', methods=['GET'])
def get_users():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        conn.close()
        
        return jsonify([{'id': user[0], 'name': user[1], 'email': user[2]} for user in users])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 