from ...db.tbl.GT import temp
tbl_temp = temp.get_tbl()
def delete_temp(id):
    tbl_temp.delete_many({"ConfigID": id})

def set_bot_active(in_id, in_bool):
    query_where = {"ConfigID" : in_id}
    value_update = {"$set":  in_bool}
    tbl_temp.update_many(query_where, value_update)