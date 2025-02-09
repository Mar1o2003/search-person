import logging
from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')


db = SQLAlchemy(app)
api = Api(app)


logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.before_request
def log_request_info():
    logging.info(
        f"Request: {request.method} {request.url} - Params: {request.args.to_dict()} - Body: {request.get_json(silent=True)}"
    )

from app import resources