# -*- coding:utf-8 -*-
import os
import logging
from uuid import uuid4
from datetime import datetime

from flask import *
from flask_jsonrpc import JSONRPC
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, create_engine

def create_db(app,metadata):
    db = SQLAlchemy(app,metadata=metadata,session_options={'autocommit':False},use_native_unicode=True)
    return db

def init_app():
    app = Flask(__name__)
    app.config.from_object('api.config')
    app.debug_log_format = "%(levelname)s in %(module)s [%(lineno)d]: %(message)s"
    metadata = MetaData()
    db = create_db(app,metadata)
    return app, metadata,db

app, metadata, db = init_app()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

jsonrpc = JSONRPC(app, '/api',enable_web_browsable_api=True)
 
#db.create_all() 

# --------- API -----------

from api.admin import *
from api.ftom import *

# --------- API -----------
 
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__z':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()




