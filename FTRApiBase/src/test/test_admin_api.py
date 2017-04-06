import sys
sys.path.insert(0,".")
sys.path.insert(0,"..")
from test.utils import rpc_call
from pprint import pprint, pformat
from flask_jsonrpc.proxy import ServiceProxy

AZURE = "http://ftr-app.japanwest.cloudapp.azure.com:5000"
LOCAL = "http://localhost:5000"

# SERVER_URL = AZURE
# 
# SERVICE_PROXY = SERVER_URL + "/api"
# 
# server = ServiceProxy(SERVICE_PROXY)
# cmm_index = server.cmm.index
# 
# r = rpc_call(cmm_index)
# print(pformat(r))

class TestCmmServiceProxy(object):
    SERVER_URL = LOCAL

    def __init__(self,server_url=None):
        if server_url is not None:
            self.SERVER_URL = server_url

    def serviceProxy(self):
        return ServiceProxy(self.SERVER_URL + '/api')

    def comm_index(self):
        print("=============== CALL<{}> ===============".format(self.SERVER_URL))
        server = self.serviceProxy()
        r = rpc_call(server.cmm.index)
        print(pformat(r))
        print("=============== CALL<{}> ===============".format(self.SERVER_URL))
    
if __name__ == '__main__':
    tester = TestCmmServiceProxy()
#     tester.SERVER_URL = LOCAL
    tester.SERVER_URL = AZURE
    tester.comm_index()
    
