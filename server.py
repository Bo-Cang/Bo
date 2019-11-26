import bottle
from bottle import route
import os
from datetime import datetime as dt
from random import randrange

from bottle import route, run, static_file, view
@route('/')
def index():
  return '<p>H123ello</p>'

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
