from ...db.tbl.ST import config
from bson.objectid import ObjectId
from ...controllers import model_to_json as md_convert
from ...controllers import file

tbl_config = config.get_tbl()

def update(id_update, value_update):
    query_where = {"_id" : ObjectId(id_update)}
    tbl_config.update_one(query_where, { "$set": value_update })

def add(in_model):
    tbl_config.insert_one(in_model)

def get_all():
    return md_convert.st_configs(tbl_config.find())

def get_simple(id_find):
    query_where = {"_id" : ObjectId(id_find)}
    return md_convert.st_config(tbl_config.find_one(query_where))

def check_exist(in_crypto_name):
    query_where = {"CryptoName" : in_crypto_name}
    if(tbl_config.find_one(query_where)):
        return True
    return False
