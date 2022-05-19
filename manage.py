from app import create_app
from flask_script import Manager,Server
from app import create_app,db
from app.models import *
from flask_migrate import Migrate,MigrateCommand

app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)
migrate=Migrate(app,db)
@manager.command
def test():
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Customer=Customer )

if __name__ == '__main__':
    manager.run()