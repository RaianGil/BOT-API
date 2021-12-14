from ...models.ST import bot
import json
from ...controllers import file, process
from flask import request

def run(api):
    app = api

    @app.route('/api/ST/bot', methods=['GET'])
    def find_st_bot_all():
        datos = bot.get_all()
        return datos
    
    @app.route('/api/ST/bot/<id>', methods=['GET'])
    def find_st_bot_single(id):
        datos = bot.get_simple(id)
        return datos

    @app.route('/api/ST/bot/<id>', methods=['PUT'])
    def update_st_bot_single(id):
        return_msg = process.to_st_bot(id, request.form)
        return json.dumps(return_msg)