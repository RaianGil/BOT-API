import config
from pymongo import MongoClient

host = config.server_host
port = config.server_port

def get():
    return MongoClient(host, port)