from dotenv import load_dotenv, find_dotenv
from os import environ

load_dotenv(find_dotenv())

SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
SECRET_KEY = environ.get("SECRET_KEY")
