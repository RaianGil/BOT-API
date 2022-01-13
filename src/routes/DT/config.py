from ...models.DT import config
import json
from ...controllers import file, process
from flask import request

def run(api):
    app = api
    @app.route('/api/DT/config', methods=['GET'])
    def find_dt_config_all():
        datos = config.get_all()
        return datos
    
    @app.route('/api/DT/config/<id>', methods=['GET'])
    def find_dt_config_single(id):
        datos = config.get_simple(id)
        return datos

    @app.route('/api/DT/config/<id>', methods=['PUT'])
    def update_dt_config_single(id):
        return_msg = process.to_dt_config(id, request.json)
        return json.dumps(return_msg)
    
    @app.route('/api/DT/config/<id>', methods=['DELETE'])
    def disable_dt_config(id):
        return_msg = process.disable_dt_config(id)
        return json.dumps(return_msg)

    @app.route('/api/DT/config', methods=['POST'])
    def add_dt_config_single():
        return_msg = process.new_dt_config(request.json)
        return json.dumps(return_msg)