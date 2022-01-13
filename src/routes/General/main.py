from ...models import virt_wallet
import json
 
from flask import request

def run(api):
    app = api
    @app.route('/api/Virt/balance', methods=['GET'])
    def get_balance():
        datos = virt_wallet.get_balances()
        return datos
    @app.route('/api/Virt/gain', methods=['GET'])
    def get_gain():
        datos = virt_wallet.get_gain()
        return datos