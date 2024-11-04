from flask import Flask
from src.views.restuarant import Usertemp as temp_blueprint
from src.config import app_config


def create_app(env_name):
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    # bcrypt.init_app(app)
    # db.init_app(app)
    # cors.init_app(app)

    # app.register_blueprint(user_blueprint, url_prefix='/api/')
    app.register_blueprint(temp_blueprint, url_prefix='/temp/')
    return app 
