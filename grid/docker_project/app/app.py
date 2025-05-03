from flask import Flask, jsonify, request
import sqlite3
import os

app = Flask(__name__)

# Путь к файлу базы данных (монтируется через docker-compose)
DB_PATH = '/data/database.db'

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
            conn.close()
            
            return jsonify([{'id': user[0], 'name': user[1], 'email': user[2]} for user in users])
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    elif request.method == 'POST':
        try:
            data = request.get_json()
            name = data.get('name')
            email = data.get('email')
            
            if not name or not email:
                return jsonify({'error': 'Name and email are required'}), 400
                
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
            conn.commit()
            user_id = cursor.lastrowid
            conn.close()
            
            return jsonify({'id': user_id, 'name': name, 'email': email}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
        
        return jsonify({'message': f'User with id {user_id} deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 