# from app.models import User_data, Car_data
from flask_jsonschema import validate
import urllib
import requests
from app import app, db
from app.schema_validation import *
import json
from flask import request
from flask_bcrypt import Bcrypt
