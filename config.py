import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

server_host = os.environ.get("SERVER_HOST", "127.0.0.1")
db_bot = os.environ.get("BOTS_DB", "DB_BOTS")
db_virt_wallet = os.environ.get("DB_NAME", "DB_SMD")

try:
    server_port = int(os.environ.get("SERVER_PORT", 27017))
except:
    server_port = 27017