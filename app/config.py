import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1@localhost:5432/ern_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False