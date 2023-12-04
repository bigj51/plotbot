import os

class Config:
    """Base config class."""
    def __init__(self):
        self.OPENAI_KEY = None

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def OPENAI_KEY(self):
        if os.environ.get('OPENAI_KEY'):
            return os.environ.get('OPENAI_KEY')
        else:
            from keys import OPENAI_KEY
            return OPENAI_KEY

class Prod(Config):
    """Production specific config."""
    DEBUG = False

class Dev(Config):
    """Development environment specific configuration."""
    DEBUG = True
    TESTING = True

class Test(Config):
    """Testing environment specific configuration."""
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
