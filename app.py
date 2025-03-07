from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
    c.execute('INSERT INTO users VALUES ("admin", "FLAG{BackdoorSQL}")')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    c.execute(query)
    result = c.fetchone()
    conn.close()
    if result:
        return "Logged in! " + result[1]  # Reveals flag
    return "Login failed."

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8000)