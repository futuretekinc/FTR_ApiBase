import logging
from pprint import pformat, pprint
from flask_jsonrpc.proxy import ServiceProxy

logger = logging.getLogger(__name__)

AZURE = "http://ftr-app.japanwest.cloudapp.azure.com:5000"
LOCAL = "http://localhost:5000"

SERVER_URL = AZURE
API_URI = '/api'

server = ServiceProxy(SERVER_URL + API_URI)

def call_debug(func,*args,**kwargs):
	def wrap():
		print("")
		print("-"*80)
		print(" METHOD - {}".format(func.__name__))
		print(" API_SERVER - {}".format(SERVER_URL))
		print("-"*80)
		r = func(*args,**kwargs)
		print("[ result ]")
		print(pformat(r))
		print("")
	return wrap

def rpc_call(func,*args,**kwargs):
    try:
        logger.info("--CALL")
        r = func(*args,**kwargs)
        logger.info(r)
        if 'error' in r:
            return r.get('error').get('name')
        else:
            return r.get('result')
    except Exception as e:
        logger.error(e)
        return None

