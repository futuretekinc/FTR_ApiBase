from api import app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__z':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()
