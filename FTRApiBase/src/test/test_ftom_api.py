#!/home/ftr/anaconda3/envs/python34/bin/python
import sys
sys.path.insert(0,".")
sys.path.insert(0,"..")
from test.utils import rpc_call
from pprint import pprint, pformat
from flask_jsonrpc.proxy import ServiceProxy

AZURE = "http://ftr-app.japanwest.cloudapp.azure.com:5000"
LOCAL = "http://localhost:5000"

class TestFtomServiceProxy(object):
    SERVER_URL = LOCAL

    def __init__(self,server_url=None):
        if server_url is not None:
            self.SERVER_URL = server_url

    def serviceProxy(self):
        return ServiceProxy(self.SERVER_URL + '/api')

    def get_eptype(self):
        print("=============== CALL<{}> ===============".format(self.SERVER_URL))
        server = self.serviceProxy()
        #r = server.obm.get.eptype()
        #print(pformat(r))
        r = rpc_call(server.obm.get.eptype)
        print(pformat(r))
        print("=============== CALL<{}> ===============".format(self.SERVER_URL))
    
if __name__ == '__main__':
    tester = TestFtomServiceProxy()
#     tester.SERVER_URL = LOCAL
    tester.SERVER_URL = AZURE
    tester.get_eptype()
    
