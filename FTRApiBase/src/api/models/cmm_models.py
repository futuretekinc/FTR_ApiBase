from api import jsonrpc, db
from marshmallow_sqlalchemy import ModelSchema

'''
----------------------------------------------------------------------
COMMON-MODELS
----------------------------------------------------------------------
'''

class CM_CODEM(db.Model):
    __tablename__ = 'CM_CODEM'
    __table_args__ = {
        'autoload' : True,
#         'schema' : 'appdb',
        'autoload_with': db.engine
    }
    
class SCH_CM_CODEM(ModelSchema):
    class Meta:
        model = CM_CODEM
        
sch_cm_codem = SCH_CM_CODEM(many=True)



class CM_CODED(db.Model):
    __tablename__ = 'CM_CODED'
    __table_args__ = {
        'autoload' : True,
        'autoload_with': db.engine
    }
    
class SCH_CM_CODED(ModelSchema):
    class Meta:
        model = CM_CODED
        
sch_cm_coded = SCH_CM_CODED(many=True)


