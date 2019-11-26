import bottle
from bottle import route
@route('/')
def index():
  return '<p>H123ello</p>'

if __name__ == '__main__':
  run(application=APP)
