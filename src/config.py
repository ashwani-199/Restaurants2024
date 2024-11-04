import os
from dotenv import load_dotenv
load_dotenv()

class Development(object):
    """
    Development environment configurations
    """
     
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_BINDS = {
        'django_test': SQLALCHEMY_DATABASE_URI
    }
    SQLALCHEMY_ECHO = False


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_BINDS = {
        'django_test': SQLALCHEMY_DATABASE_URI
    }
    SQLALCHEMY_ECHO = False


app_config = {
    'development': Development,
    'production': Production,
}
