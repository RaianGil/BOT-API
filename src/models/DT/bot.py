from ...db.tbl.DT import bot
from bson.objectid import ObjectId
from ...controllers import file

tbl_bot = bot.get_tbl()
def update_percent(id_update, in_percent):
    query_where = {"_id" : ObjectId(id_update)}
    bot_start = tbl_bot.find_one(query_where).get("BotStart")
    bot_stop = bot_start * float(1+(in_percent/100))
    values_update = {"$set": { "BotStop" : bot_stop, "BotPercent" : in_percent}}
    tbl_bot.update_one(query_where, values_update)

def get_all():
    return file.to_json(tbl_bot.find())

def get_simple(id_find):
    query_where = {"_id" : ObjectId(id_find)}
    return file.to_json(tbl_bot.find_one(query_where))