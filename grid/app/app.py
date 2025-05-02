from flask import Flask, jsonify, request
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

# Путь к файлу базы данных (монтируется через docker-compose)
DB_PATH = '/data/database.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/users', methods=['GET'])
def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        conn.close()
        
        return jsonify([dict(user) for user in users])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Missing required fields'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)',
                      (data['name'], data['email']))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()

        return jsonify({'id': user_id, 'name': data['name'], 'email': data['email']}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already exists'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/messages', methods=['GET'])
def get_messages():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT m.id, m.message, m.created_at, u.name as user_name, u.email
            FROM messages m
            JOIN users u ON m.user_id = u.id
            ORDER BY m.created_at DESC
        ''')
        messages = cursor.fetchall()
        conn.close()
        
        return jsonify([dict(msg) for msg in messages])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 