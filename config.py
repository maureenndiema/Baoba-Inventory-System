import os

class Config:
    debug = True
    
    SECRET_KEY ='1234'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://riziki:riziki@localhost/baoba'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:wambui@localhost/baoba'
    # ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://riziki:riziki@localhost/baoba'

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://riziki:riziki@localhost/baoba'

    DEBUG = True
    ENV = 'development'

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}