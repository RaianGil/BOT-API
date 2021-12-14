from ...models.DT import bot
import json
from ...controllers import file, process
from flask import request

def run(api):
    app = api
    @app.route('/api/DT/bot', methods=['GET'])
    def find_dt_bot_all():
        datos = bot.get_all()
        return datos
    
    @app.route('/api/DT/bot/<id>', methods=['GET'])
    def find_dt_bot_single(id):
        datos = bot.get_simple(id)
        return datos

    @app.route('/api/DT/bot/<id>', methods=['PUT'])
    def update_dt_bot_single(id):
        return_msg = process.to_dt_bot(id, request.form)
        return json.dumps(return_msg)