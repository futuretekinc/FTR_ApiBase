from test.utils import rpc_call
from pprint import pprint, pformat
from flask_jsonrpc.proxy import ServiceProxy

server = ServiceProxy('http://localhost:5000/api')
cmm_index = server.cmm.index

r = rpc_call(cmm_index)
print(pformat(r))


