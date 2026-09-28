from werkzeug.security import generate_password_hash, check_password_hash
import db

def register(username, password, user_type):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash, user_type) VALUES (?, ?, ?)"
    db.execute(sql, [username, password_hash, user_type])

def login(username, password):
    sql = "SELECT password_hash FROM users WHERE username = ?"
    password_hash = db.query(sql, [username])[0][0]

    if check_password_hash(password_hash, password):
        return True