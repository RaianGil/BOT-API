from . import mongo_client
import config

conn = mongo_client.get()

db_name = config.db_bot
db_wallet = config.db_virt_wallet

def ST():
    return conn[db_name]

def DT():
    return conn[db_name]

def Transaction():
    print(db_wallet)
    return conn[db_wallet]