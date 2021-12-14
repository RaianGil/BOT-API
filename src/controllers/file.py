from bson.json_util import dumps

confirm_list = ['true', '1', 't', 'si', 's', 'yes', 'y', 'active', 'activo']

def to_json(in_mongo):
    json_return = list(in_mongo)
    return dumps(json_return)

def to_bool(in_bool):
    return in_bool.lower() in confirm_list
    
def to_bit(in_bool):
    if(in_bool.lower() not in confirm_list):
        return 0
    return 1    