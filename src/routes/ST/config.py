from ...models.ST import config
import json
from ...controllers import file, process
from flask import request

def run(api):
    app = api
    @app.route('/api/ST/config', methods=['GET'])
    def find_st_config_all():
        datos = config.get_all()
        return datos
    
    @app.route('/api/ST/config/<id>', methods=['GET'])
    def find_st_config_single(id):
        datos = config.get_simple(id)
        return datos

    @app.route('/api/ST/config/<id>', methods=['PUT'])
    def update_st_config_single(id):
        return_msg = process.to_st_config(id, request.form)
        return json.dumps(return_msg)

    @app.route('/api/ST/config', methods=['POST'])
    def add_st_config_single():
        return_msg = process.new_st_config(request.form)
        return json.dumps(return_msg)