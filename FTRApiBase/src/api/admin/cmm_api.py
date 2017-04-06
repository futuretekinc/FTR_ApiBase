from api import jsonrpc, db
from api.models import *

@jsonrpc.method('cmm.index')
def index():
    r = db.session.query(CM_CODEM).all() 
    result = sch_cm_codem.dump(r)
    return { 'data' : result.data } 

