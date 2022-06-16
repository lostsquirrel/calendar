from gevent.pywsgi import WSGIServer
from app import app

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 8000), app)
    http_server.serve_forever()
