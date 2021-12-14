from ...db.tbl.ST import config
from bson.objectid import ObjectId
from ...controllers import file

tbl_config = config.get_tbl()

def update(id_update, value_update):
    query_where = {"_id" : ObjectId(id_update)}
    tbl_config.update_one(query_where, value_update)

def add(in_model):
    tbl_config.insert_one({
        "CryptoName" : in_model.crypto_name,
        "CryptoSymbol": in_model.crypto_symbol,
        "BotBuy": in_model.bot_buy,
        "BotLimitBuy": in_model.bot_limit_buy,
        "BotSell": in_model.bot_sell,
        "BotAmount": in_model.bot_amount,
        "BotAmountLimit": in_model.bot_amount_limit,
        "IsRealAccount": in_model.is_real_account,
        "BotActive": in_model.bot_active,
        "InOrder": False
        })

def get_all():
    return file.to_json(tbl_config.find())

def get_simple(id_find):
    query_where = {"_id" : ObjectId(id_find)}
    return file.to_json(tbl_config.find_one(query_where))

def check_exist(in_crypto_name):
    query_where = {"CryptoName" : in_crypto_name}
    if(tbl_config.find_one(query_where)):
        return True
    return False
