import bottle, route

APP = Bottle()

@APP.get('/')
def index():
  return '<p>H123456789ello</p>'

if __name__ == '__main__':
  run(application=APP)
