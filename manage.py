from app import create_app
from flask_script import Manager,Server
from app import create_app,db
from app.models import User
from flask_migrate import Migrate,MigrateCommand