from ...db.tbl.DT import config
from bson.objectid import ObjectId
from ...controllers import file

tbl_config = config.get_tbl()

def update(id_update, value_update):
    query_where = {"_id" : ObjectId(id_update)}
    tbl_config.update_one(query_where, value_update)

def get_all():
    return file.to_json(tbl_config.find())

def get_simple(id_find):
    query_where = {"_id" : ObjectId(id_find)}
    return file.to_json(tbl_config.find_one(query_where))