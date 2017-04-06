#!/home/ftr/anaconda3/envs/python34/bin/python
from api import jsonrpc, db
from api.models import *

import decimal
import json

def decimal_default(obj):
	if isinstance(obj,decimal.Decimal):
		return str(float(obj))
	raise TypeError

@jsonrpc.method('obm.get.eptype')
def get_eptype():
	r = db.session.query(OB_ENDPOINT_TYPE).all()
	print(r)
	result = sch_ob_endpoint_type.dump(r) 
	return json.dumps({ 'data' : result.data },default=decimal_default)


class ObEndpointTypeHandler(object):

	@classmethod
	@jsonrpc.method('obm.save.eptype')
	def do_update(param=None):
		return json.dumps({'data' : { 'action' : 'update', 'result' : True } })

	@classmethod
	def do_save(param=None):
		pass

	@classmethod
	def do_read(param=None):
		pass
