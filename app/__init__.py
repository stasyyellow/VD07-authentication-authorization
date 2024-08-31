import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Инициализируем Migrate
    migrate = Migrate(app, db)

    # Настройка LoginManager
    login_manager.login_view = 'routes.login'
    login_manager.login_message_category = 'info'

    # Переносим импорт routes сюда, после создания app
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
