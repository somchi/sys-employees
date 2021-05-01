import os
from decouple import config as env_config


BASEDIR = os.getcwd()
WORKDIR = os.path.abspath(os.path.dirname(__file__))

FLASK_ENV = env_config("FLASK_ENV")
FLASK_APP = env_config("FLASK_APP")
FLASK_RUN_PORT = env_config("FLASK_RUN_PORT")
SECRET_KEY = env_config("SECRET_KEY")
DEBUG = True
JWT_SECRET_KEY = env_config("JWT_SECRET_KEY")
LOG_LEVEL = "DEBUG"

