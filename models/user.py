from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    users = {
        "admin": {
            "id": "admin",
            "username": "admin",
            "password_hash": generate_password_hash("password123")
        }
    }

    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    @classmethod
    def get(cls, user_id):
        user = cls.users.get(user_id)
        if user:
            return User(user["id"], user["username"], user["password_hash"])
        return None

    @classmethod
    def authenticate(cls, username, password):
        user = cls.users.get(username)
        if user and check_password_hash(user["password_hash"], password):
            return User(user["id"], user["username"], user["password_hash"])
        return None

    @classmethod
    def register(cls, username, password):
        if username in cls.users:
            return None
        cls.users[username] = {
            "id": username,
            "username": username,
            "password_hash": generate_password_hash(password)
        }
        return User.get(username)
