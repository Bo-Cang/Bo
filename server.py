import bottle, route

APP = Bottle()

@APP.route('/')
def index():
  return '<p>H123456789ello</p>'

if __name__ == '__main__':
  APP.run()
