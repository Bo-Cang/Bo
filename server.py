import bottle, route

APP = bottle.Bottle()

@APP.get('/')
def index():
  return '<p>H123456789ello</p>'

if __name__ == '__main__':
  bottle.run(application=APP)
