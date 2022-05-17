from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from flask_uploads import IMAGES, UploadSet,configure_uploads
from flask_mail import Mail


bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://maureen:1234@localhost/baoba'


    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # from .auth import auth as authentication_blueprint
    # app.register_blueprint(authentication_blueprint, url_prefix='/authenticate')

    return app