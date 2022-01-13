from flask import jsonify
from bson.objectid import ObjectId

def dt_configs(in_model):
    dtconfigs = []
    for dtconfig in in_model:
        dtconfigs.append({
            '_id': str(ObjectId(dtconfig['_id'])),
            'bot_name': dtconfig['BotName'],
            'crypto_symbol': dtconfig['CryptoSymbol'],
            'bot_min_buy': dtconfig['BotMinBuy'],
            'bot_next_buy': dtconfig['BotNextBuy'],
            'bot_percent': dtconfig['BotPercent'],
            'bot_decay': dtconfig['BotDecay'],
            'bot_amount': dtconfig['BotAmount'],
            'amount_limit': dtconfig['AmountLimit'],
            'bot_active': dtconfig['BotActive']
        })
    return jsonify(dtconfigs)

def dt_config(in_model):
    dtconfig = {
        '_id': str(ObjectId(in_model['_id'])),
        'bot_name': in_model['BotName'],
        'crypto_symbol': in_model['CryptoSymbol'],
        'bot_min_buy': in_model['BotMinBuy'],
        'bot_next_buy': in_model['BotNextBuy'],
        'bot_percent': in_model['BotPercent'],
        'bot_decay': in_model['BotDecay'],
        'bot_amount': in_model['BotAmount'],
        'amount_limit': in_model['AmountLimit'],
        'bot_active': in_model['BotActive']
    }
    return jsonify(dtconfig)

def st_configs(in_model):
    stconfigs = []
    for stconfig in in_model:
        stconfigs.append({
            '_id': str(ObjectId(stconfig['_id'])),
            'bot_name': stconfig['BotName'],
            'crypto_symbol': stconfig['CryptoSymbol'],
            'bot_buy': stconfig['BotBuy'],
            'bot_limit_buy': stconfig['BotLimitBuy'],
            'bot_sell': stconfig['BotSell'],
            'bot_amount': stconfig['BotAmount'],
            'amount_limit': stconfig['BotAmountLimit'],
            'bot_active': stconfig['BotActive'],
            'in_order': stconfig['InOrder']
        })
    return jsonify(stconfigs)

def st_config(in_model):
    stconfig = {
        '_id': str(ObjectId(in_model['_id'])),
        'bot_name': in_model['BotName'],
        'crypto_symbol': in_model['CryptoSymbol'],
        'bot_buy': in_model['BotBuy'],
        'bot_limit_buy': in_model['BotLimitBuy'],
        'bot_sell': in_model['BotSell'],
        'bot_amount': in_model['BotAmount'],
        'amount_limit': in_model['BotAmountLimit'],
        'bot_active': in_model['BotActive'],
        'in_order': in_model['InOrder']
    }
    return jsonify(stconfig)


def gt_configs(in_model):
    gtconfigs = []
    for gtconfig in in_model:
        gtconfigs.append({
            '_id': str(ObjectId(gtconfig['_id'])),
            'bot_name': gtconfig['BotName'],
            'crypto_symbol': gtconfig['CryptoSymbol'],
            'min_price': gtconfig['MinPrice'],
            'max_price': gtconfig['MaxPrice'],
            'amount_limit': gtconfig['AmountLimit'],
            'grid_number': gtconfig['GridNumber'],
            'grid_percent': gtconfig['GridPercent'],
            'bot_active': gtconfig['BotActive']
        })
    return jsonify(gtconfigs)

def gt_config(in_model):
    gtconfig = {
        '_id': str(ObjectId(in_model['_id'])),
        'bot_name': in_model['BotName'],
        'crypto_symbol': in_model['CryptoSymbol'],
        'min_price': in_model['MinPrice'],
        'max_price': in_model['MaxPrice'],
        'amount_limit': in_model['AmountLimit'],
        'grid_number': in_model['GridNumber'],
        'grid_percent': in_model['GridPercent'],
        'bot_active': in_model['BotActive']
    }
    return jsonify(gtconfig)