from ...db.tbl.GT import config
from bson.objectid import ObjectId
from ...controllers import file
from ...controllers import model_to_json

tbl_config = config.get_tbl()
md_convert = model_to_json

def update(id_update, value_update):
    query_where = {"_id" : ObjectId(id_update)}
    tbl_config.update_one(query_where, { "$set": value_update })

def add(in_model):
    tbl_config.insert_one(in_model)

def get_all():
    data = tbl_config.find()
    return md_convert.gt_configs(data)

def get_simple(id_find):
    query_where = {"_id" : ObjectId(id_find)}
    return md_convert.gt_config(tbl_config.find_one(query_where))

def check_exist(in_bot_name):
    query_where = {"BotName" : in_bot_name}
    if(tbl_config.find_one(query_where)):
        return True
    return False