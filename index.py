from src.routes import main
from src.routes.DT import config as dt_config
from src.routes.DT import bot as dt_bot
from src.routes.ST import config as st_config
from src.routes.ST import bot as st_bot
api = main.get()
# Daily Trade routes
dt_config.run(api)
dt_bot.run(api)
st_config.run(api)
st_bot.run(api)
# Simple Trade routes
api.run()