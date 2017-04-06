#!/home/ftr/anaconda3/envs/python34/bin/python
import sys
sys.path.insert(0,".")
sys.path.insert(0,"..")
from test.utils import rpc_call, call_debug, server


@call_debug
def obm_get_eptype():
	return rpc_call(server.obm.get.eptype)

@call_debug
def obm_save_eptype():
	return rpc_call(server.obm.save.eptype)

    
if __name__ == '__main__':
	obm_get_eptype()
	obm_save_eptype()
    
