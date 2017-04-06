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
