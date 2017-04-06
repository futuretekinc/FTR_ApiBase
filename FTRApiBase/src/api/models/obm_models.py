from api import jsonrpc, db
from marshmallow_sqlalchemy import ModelSchema


class OB_RESOURCE(db.Model):
    __tablename__ = 'OB_RESOURCE'
    __table_args__ = {
        'autoload' : True,
        'autoload_with': db.engine
    }
    
class SCH_OB_RESOURCE(ModelSchema):
    class Meta:
        model = OB_RESOURCE
        
sch_ob_resource = SCH_OB_RESOURCE(many=True)



class OB_GATEWAY(db.Model):
    __tablename__ = 'OB_GATEWAY'
    __table_args__ = {
        'autoload' : True,
        'autoload_with': db.engine
    }
    
class SCH_OB_GATEWAY(ModelSchema):
    class Meta:
        model = OB_GATEWAY
        
sch_ob_gateway = SCH_OB_GATEWAY(many=True)



class OB_ENDPOINT_TYPE(db.Model):
    __tablename__ = 'OB_ENDPOINT_TYPE'
    __table_args__ = {
        'autoload' : True,
        'autoload_with': db.engine
    }
    
class SCH_OB_ENDPOINT_TYPE(ModelSchema):
    class Meta:
        model = OB_ENDPOINT_TYPE
        
sch_ob_endpoint_type = SCH_OB_ENDPOINT_TYPE(many=True)



class OB_ENDPOINT(db.Model):
    __tablename__ = 'OB_ENDPOINT'
    __table_args__ = {
        'autoload' : True,
        'autoload_with': db.engine
    }
    
class SCH_OB_ENDPOINT(ModelSchema):
    class Meta:
        model = OB_ENDPOINT
        
sch_ob_endpoint = SCH_OB_ENDPOINT(many=True)



class OB_DEVICE_TYPE_MAP(db.Model):
    __tablename__ = 'OB_DEVICE_TYPE_MAP'
    __table_args__ = {
        'autoload' : True,
        'autoload_with': db.engine
    }
    
class SCH_OB_DEVICE_TYPE_MAP(ModelSchema):
    class Meta:
        model = OB_DEVICE_TYPE_MAP
        
sch_ob_device_type_map = SCH_OB_DEVICE_TYPE_MAP(many=True)



class OB_DEVICE_TYPE(db.Model):
    __tablename__ = 'OB_DEVICE_TYPE'
    __table_args__ = {
        'autoload' : True,
        'autoload_with': db.engine
    }
    
class SCH_OB_DEVICE_TYPE(ModelSchema):
    class Meta:
        model = OB_DEVICE_TYPE
        
sch_ob_device_type = SCH_OB_DEVICE_TYPE(many=True)



class OB_DEVICE(db.Model):
    __tablename__ = 'OB_DEVICE'
    __table_args__ = {
        'autoload' : True,
        'autoload_with': db.engine
    }
    
class SCH_OB_DEVICE(ModelSchema):
    class Meta:
        model = OB_DEVICE
        
sch_ob_device = SCH_OB_DEVICE(many=True)


