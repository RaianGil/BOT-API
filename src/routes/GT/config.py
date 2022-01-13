from ...models.GT import config
import json
from flask_cors import CORS
from ...controllers import file, process
from flask import request

def run(api):
    app = api
    CORS(app)
    @app.route('/api/GT/config', methods=['GET'])
    def find_gt_config_all():
        datos = config.get_all()
        return datos
    
    @app.route('/api/GT/config/<id>', methods=['GET'])
    def find_gt_config_single(id):
        datos = config.get_simple(id)
        return datos

    @app.route('/api/GT/config/<id>', methods=['PUT'])
    def update_gt_config_single(id):
        return_msg = process.to_gt_config(id, request.json)
        return json.dumps(return_msg)

    @app.route('/api/GT/config/<id>', methods=['DELETE'])
    def disable_gt_config(id):
        return_msg = process.disable_gt_config(id)
        return json.dumps(return_msg)

    @app.route('/api/GT/config', methods=['POST'])
    def add_gt_config_single():
        print(request.json)
        return_msg = process.new_gt_config(request.json)
        return json.dumps(return_msg)