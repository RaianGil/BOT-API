from . import mongo_client
import config

conn = mongo_client.get()

db_name = config.db_bot
def ST():
    return conn[db_name]

def DT():
    return conn[db_name]