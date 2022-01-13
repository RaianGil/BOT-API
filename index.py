from src.routes import main
from src.routes.GT import config as gt_config
from src.routes.General import main as general
from src.routes.DT import config as dt_config
from src.routes.DT import bot as dt_bot
from src.routes.ST import config as st_config
from src.routes.ST import bot as st_bot
from flask_cors import CORS
api = main.get()

CORS(api)
# Daily Trade routes
general.run(api)
gt_config.run(api)
dt_config.run(api)
dt_bot.run(api)
st_config.run(api)
st_bot.run(api)
# Simple Trade routes
api.run()