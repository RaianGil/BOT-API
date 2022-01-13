from os import error
from ..models.DT import config as dt_config
from ..models.DT import bot as dt_bot
from ..models.DT import model as dt_model
from ..models.ST import config as st_config
from ..models.ST import bot as st_bot
from ..models.ST import model as st_model
from ..models.GT import config as gt_config
from ..models.GT import model as gt_model
from ..models.GT import temp as gt_temp
from ..models import error as err
from ..models import success as succ

from . import file
#region DailyTrade

#PUT: /api/DT/config/<id> Update single config
def to_dt_config(id_update, in_process):
    to_update = {}
    try:
        if(dt_config.check_exist(in_process['bot_name'].upper())):
            return err.e2121
        to_update['BotName'] = in_process['bot_name'].upper()
    except:
        None

    try:
        to_update['BotMinBuy'] = float(in_process['bot_min_buy'])
    except:
        None
    try:
        to_update['BotNextBuy'] = float(in_process['bot_next_buy'])
    except:
        None
    try:
        to_update['BotPercent'] = float(in_process['bot_percent'])
    except:
        None
    try:
        to_update['BotDecay'] = float(in_process['bot_decay'])
    except:
        None
    try:
        to_update['BotAmount'] = float(in_process['bot_amount'])
    except:
        None
    try:
        to_update['AmountLimit'] = float(in_process['amount_limit'])
    except:
        None
    try:
        to_update['BotActive'] = file.to_bool(in_process['bot_active'])
    except:
        None

    try:
        dt_config.update(id_update, to_update)
    except OSError as Peter:
        print(Peter.args)
        return err.e9000
    return succ.s9000
# DELETE: /api/DT/bot/<id> Update single bot
def disable_dt_config(id_update):
    to_update = {}
    to_update['BotActive'] = False
    try:
        dt_config.update(id_update, to_update)
    except OSError as Peter:
        print(Peter.args)
        return err.e9000
    return succ.s9000

# PUT: /api/DT/bot/<id> Update single bot
def to_dt_bot(id_update, in_process):

    try:
        bot_percent = float(in_process['BotPercent'])
        dt_bot.update_percent(id_update, bot_percent)
    except:
        return err.e9000
    return succ.s9000

# POST: /api/DT/bot/ add single config
def new_dt_config(in_process):
    to_insert = {}
    print(in_process['bot_name'])
    try:
        if(dt_config.check_exist(in_process['bot_name'].upper())):
            return err.e2121
        to_insert['BotName'] = in_process['bot_name'].upper()
    except:
        print('BotName')
        return err.e1501

    try:
        to_insert['CryptoSymbol'] = in_process['crypto_symbol'].upper()
    except:
        print('CryptoSymbol')
        return err.e1502
    try:
        to_insert['BotMinBuy'] = float(in_process['bot_min_buy'])
    except:
        print('BotMinBuy')
        return err.e1503
    try:
        to_insert['BotNextBuy'] = float(in_process['bot_next_buy'])
    except:
        print('BotNextBuy')
        return err.e1504
    try:
        to_insert['BotPercent'] = float(in_process['bot_percent'])
    except:
        print('BotPercent')
        return err.e1505
    try:
        to_insert['BotDecay'] = float(in_process['bot_decay'])
    except:
        print('BotDecay')
        return err.e1506
    try:
        to_insert['BotAmount'] = float(in_process['bot_amount'])
    except:
        print('BotAmount')
        return err.e1507
    try:
        to_insert['AmountLimit'] = float(in_process['amount_limit'])
    except:
        print('AmountLimit')
        return err.e1508
    try:
        to_insert['BotActive'] = file.to_bool(in_process['bot_active'])
    except:
        print('BotActive')
        return err.e1509
    try:
        to_insert['RealAccount'] = file.to_bit(in_process['RealAccount'])
    except:
        None

    try:
        dt_config.add(to_insert)
    except:
        return err.e9000
    
    
    return succ.s9000


#endregion
#region SimpleTrade

# POST: /api/ST/bot/ add single config
def new_st_config(in_process):
    to_insert = {}
    print(in_process['bot_name'])
    try:
        if(st_config.check_exist(in_process['bot_name'].upper())):
            return err.e2121
        to_insert['BotName'] = in_process['bot_name'].upper()
    except:
        print('BotName')
        return err.e1601

    try:
        to_insert['CryptoSymbol'] = in_process['crypto_symbol'].upper()
    except:
        print('CryptoSymbol')
        return err.e1602
    try:
        to_insert['BotBuy'] = float(in_process['bot_buy'])
    except:
        print('BotBuy')
        return err.e1603
    try:
        to_insert['BotLimitBuy'] = float(in_process['bot_buy_limit'])
    except:
        print('BotLimitBuy')
        return err.e1604
    try:
        to_insert['BotSell'] = float(in_process['bot_sell'])
    except:
        print('BotSell')
        return err.e1605
    try:
        to_insert['BotAmount'] = float(in_process['bot_amount'])
    except:
        print('BotAmount')
        return err.e1607
    try:
        to_insert['BotAmountLimit'] = float(in_process['amount_limit'])
    except:
        print('BotAmountLimit')
        return err.e1608
    try:
        to_insert['BotActive'] = file.to_bool(in_process['bot_active'])
    except:
        print('BotActive')
        return err.e1609
    try:
        to_insert['RealAccount'] = file.to_bit(in_process['RealAccount'])
    except:
        None

    to_insert['InOrder'] = False
    try:
        st_config.add(to_insert)
    except:
        return err.e9000
    
    return succ.s9000

# PUT: /api/ST/bot/<id> update single config
def to_st_config(id_update, in_process):
    try:
        if(st_config.check_exist(in_process['bot_name'].upper())):
            return err.e2121
    except:
        None

    to_update = {}
    try:
        to_update['BotBuy'] = float(in_process['bot_buy'])
    except:
        print('BotBuy')
        None
    try:
        to_update['BotLimitBuy'] = float(in_process['bot_limit_buy'])
    except:
        print('BotLimitBuy')
        None
    try:
        to_update['BotSell'] = float(in_process['bot_sell'])
    except:
        print('BotSell')
        None
    try:
        to_update['BotAmount'] = float(in_process['bot_amount'])
    except:
        print('BotAmount')
        None
    try:
        to_update['BotAmountLimit'] = float(in_process['amount_limit'])
    except:
        print('BotAmountLimit')
        None
    try:
        to_update['BotActive'] = file.to_bool(in_process['bot_active'])
    except:
        print('BotActive')
        None

    try:
        st_config.update(id_update, to_update)
    except:
        return err.e9000

    return succ.s9000

def disable_st_config(id_update):
    to_update = {}
    to_update['BotActive'] = False
    try:
        st_config.update(id_update, to_update)
    except OSError as Peter:
        print(Peter.args)
        return err.e9000
    return succ.s9000

def to_st_bot(id_update, in_process):
    to_update = {}
    try:
        to_update['BotStop'] = float(in_process['BotStop'])
    except:
        None
    try:
        to_update['BotStatus'] = file.to_bit(in_process['BotStatus'])
    except:
        None

    try:
        values_update = {"$set": to_update}
        st_bot.update(id_update, values_update)
    except:
        return err.e9000

    return succ.s9000
#endregion
#region GridTrade

#PUT: /api/GT/config/<id> Update single config
def to_gt_config(id_update, in_process):
    try:
        if(st_config.check_exist(in_process['bot_name'].upper())):
            return err.e2121
    except:
        None

    to_update = {}
    try:
        to_update['MinPrice'] = float(in_process['min_price'])
    except:
        print('MinPrice')
        None
    try:
        to_update['MaxPrice'] = float(in_process['max_price'])
    except:
        print('MaxPrice')
        None
    try:
        to_update['GridNumber'] = float(in_process['grid_number'])
    except:
        print('GridNumber')
        None
    try:
        to_update['GridPercent'] = float(in_process['grid_percent'])
    except:
        print('GridPercent')
        None
    try:
        to_update['AmountLimit'] = float(in_process['amount_limit'])
    except:
        print('AmountLimit')
        None
    try:
        to_update['BotActive'] = file.to_bool(in_process['bot_active'])
    except:
        print('BotActive')
        None

    try:
        gt_config.update(id_update, to_update)
    except:
        return err.e9000

    return succ.s9000

# PUT: /api/DT/bot/<id> Update single bot
def to_gt_bot(id_update, in_process):

    try:
        bot_percent = float(in_process['BotPercent'])
        dt_bot.update_percent(id_update, bot_percent)
    except:
        return err.e9000
    return succ.s9000

# POST: /api/GT/config/ add single config
def new_gt_config(in_process):
    to_insert = {}
    print(in_process['bot_name'])
    try:
        if(st_config.check_exist(in_process['bot_name'].upper())):
            return err.e2121
        to_insert['BotName'] = in_process['bot_name'].upper()
    except:
        print('BotName')
        return err.e1701

    try:
        to_insert['CryptoSymbol'] = in_process['crypto_symbol'].upper()
    except:
        print('CryptoSymbol')
        return err.e1702
    try:
        to_insert['MinPrice'] = float(in_process['min_price'])
    except:
        print('MinPrice')
        return err.e1703
    try:
        to_insert['MaxPrice'] = float(in_process['max_price'])
    except:
        print('MaxPrice')
        return err.e1704
    try:
        to_insert['GridNumber'] = float(in_process['grid_number'])
    except:
        print('GridNumber')
        return err.e1706
    try:
        to_insert['GridPercent'] = float(in_process['grid_percent'])
        print('bro', str(to_insert['GridPercent']))
    except:
        print('GridPercent')
        return err.e1707
    try:
        to_insert['AmountLimit'] = float(in_process['amount_limit'])
    except:
        print('AmountLimit')
        return err.e1705
    try:
        to_insert['BotActive'] = file.to_bool(in_process['bot_active'])
    except:
        print('BotActive')
        return err.e1708
    try:
        to_insert['RealAccount'] = file.to_bit(in_process['RealAccount'])
    except:
        None

    try:
        gt_config.add(to_insert)
    except:
        return err.e9000
    
    return succ.s9000

def disable_gt_config(id_update):
    to_update = {}
    to_update['BotActive'] = False
    try:
        gt_config.update(id_update, to_update)
    except OSError as Peter:
        print(Peter.args)
        return err.e9000
    return succ.s9000
#endregion
