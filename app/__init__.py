from flask import Flask
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': 'redis',
    'CACHE_REDIS_PORT': '6379',
    'CACHE_REDIS_URL': 'redis://redis:6379'
})
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db/car_model'

db = SQLAlchemy(app)

from app import views
from app import models

db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.0', threaded=True)
