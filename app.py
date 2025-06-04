from flask import Flask
from flask_login import LoginManager
from models.user import User


from controllers.auth import auth_bp
from controllers.dash import dash_bp

app = Flask(__name__)
app.secret_key = 'MthobisiNxumalo30'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

app.register_blueprint(auth_bp)
app.register_blueprint(dash_bp)

if __name__ == "__main__":
    app.run()
