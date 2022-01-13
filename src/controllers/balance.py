from . import crypto_json_cmd
from binance.client import Client
from binance.enums import *
from ..models import transaction
import config

def get(in_json):
    real_account = crypto_json_cmd.get_real_account(in_json)
    dolar_name = config.dollar_coin
    if(real_account == 1):
        client = Client(config.api_key, config.api_secret, tld='com')
        try:
            return float(client.get_asset_balance(asset=dolar_name).get('free'))
        except:
            return float(0)
    
    return transaction.get_wallet_amount(dolar_name)