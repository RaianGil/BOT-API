from ...models.DT import config
import json
from flask_cors import CORS
from ...controllers import file, process
from flask import request

def run(api):
    app = api
    CORS(app)
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
        return_msg = process.to_dt_config(id, request.form)
        return json.dumps(return_msg)