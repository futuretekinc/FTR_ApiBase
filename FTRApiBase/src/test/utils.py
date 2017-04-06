import logging
logger = logging.getLogger(__name__)

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

