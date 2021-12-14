from ..models.DT import config as dt_config
from ..models.DT import bot as dt_bot
from ..models.ST import config as st_config
from ..models.ST import bot as st_bot
from ..models.ST import model as st_model
from ..models import error as err
from ..models import success as succ

from . import file
#region DailyTrade

# PUT: /api/DT/config/<id> Update single config
def to_dt_config(id_update, in_process):
    
    next_buy = in_process.get('BotNextBuy')
    amount_limit = in_process.get('AmountLimit')
    bot_active = in_process.get('BotActive')

    try:
        if(next_buy):
            next_buy = float(in_process.get('BotNextBuy'))
            values_update = {"$set": { "BotNextBuy" : next_buy}}
            dt_config.update(id_update, values_update)

        if(amount_limit):
            amount_limit = float(in_process.get('AmountLimit'))
            values_update = {"$set": { "AmountLimit" : amount_limit}}
            dt_config.update(id_update, values_update)

        if(bot_active):
            bot_active = file.to_bool(in_process.get('BotActive'))
            values_update = {"$set": { "BotActive" : bot_active}}
            dt_config.update(id_update, values_update)
    except:
        return err.e9000
    return succ.s9000

# PUT: /api/DT/bot/<id> Update single bot
def to_dt_bot(id_update, in_process):

    try:
        bot_percent = float(in_process.get("BotPercent"))
        dt_bot.update_percent(id_update, bot_percent)
    except:
        return err.e9000
    return succ.s9000


#endregion
#region SimpleTrade

# POST: /api/ST/bot/ add single config
def new_st_config(in_process):

    if(st_config.check_exist(in_process.get('CryptoName').upper())):
        return err.e2121

    if(not in_process.get('CryptoName')):
        return err.e1601
    if(not in_process.get('CryptoSymbol')):
        return err.e1602
    if(not in_process.get('BotBuy')):
        return err.e1603
    if(not in_process.get('BotLimitBuy')):
        return err.e1604
    if(not in_process.get('BotSell')):
        return err.e1605
    if(not in_process.get('BotAmount')):
        return err.e1606
    if(not in_process.get('BotAmountLimit')):
        return err.e1607
    if(not in_process.get('IsRealAccount')):
        return err.e1608
    if(not in_process.get('BotActive')):
        return err.e1609
    try:
        st_model.crypto_name = in_process.get('CryptoName').upper()
        st_model.crypto_symbol = in_process.get('CryptoSymbol').upper()
        st_model.bot_buy = float(in_process.get('BotBuy'))
        st_model.bot_limit_buy = float(in_process.get('BotLimitBuy'))
        st_model.bot_sell = float(in_process.get('BotSell'))
        st_model.bot_amount = float(in_process.get('BotAmount'))
        
        st_model.bot_amount_limit = float(in_process.get('BotAmountLimit'))
        st_model.is_real_account = file.to_bit(in_process.get('IsRealAccount'))
        
        st_model.bot_active = file.to_bool(in_process.get('BotActive'))
        st_config.add(st_model)
        
    except:
        return err.e9000
    
    
    return succ.s9000

# PUT: /api/ST/bot/<id> update single config
def to_st_config(id_update, in_process):
    
    bot_buy = in_process.get('BotBuy')
    bot_limit_buy = in_process.get('BotLimitBuy')
    bot_sell = in_process.get('BotSell')
    bot_amount = in_process.get('BotAmount')
    bot_amount_limit = in_process.get('BotAmountLimit')
    bot_active = in_process.get('BotActive')

    try:
        if(bot_buy):
            bot_buy = float(in_process.get('BotBuy'))
            values_update = {"$set": { "BotBuy" : bot_buy}}
            st_config.update(id_update, values_update)

        if(bot_limit_buy):
            bot_limit_buy = float(in_process.get('BotLimitBuy'))
            values_update = {"$set": { "BotLimitBuy" : bot_limit_buy}}
            st_config.update(id_update, values_update)

        if(bot_sell):
            bot_sell = file.to_bool(in_process.get('BotSell'))
            values_update = {"$set": { "BotSell" : bot_sell}}
            st_config.update(id_update, values_update)

        if(bot_amount):
            bot_amount = float(in_process.get('BotAmount'))
            values_update = {"$set": { "BotAmount" : bot_amount}}
            st_config.update(id_update, values_update)

        if(bot_amount_limit):
            bot_amount_limit = float(in_process.get('BotAmountLimit'))
            values_update = {"$set": { "BotAmountLimit" : bot_amount_limit}}
            st_config.update(id_update, values_update)

        if(bot_active):
            bot_active = file.to_bool(in_process.get('BotActive'))
            values_update = {"$set": { "BotActive" : bot_active}}
            st_config.update(id_update, values_update)
    except:
        return err.e9000

    return succ.s9000

def to_st_bot(id_update, in_process):

    bot_start = in_process.get('BotStart')
    bot_stop = in_process.get('BotStop')
    bot_status = in_process.get('BotStatus')

    try:
        if(bot_start):
            bot_start = float(in_process.get('BotStart'))
            values_update = {"$set": { "BotStart" : bot_start}}
            st_bot.update(id_update, values_update)

        if(bot_stop):
            bot_stop = float(in_process.get('BotStop'))
            values_update = {"$set": { "BotStop" : bot_stop}}
            st_bot.update(id_update, values_update)

        if(bot_status):
            bot_status = file.to_bit(in_process.get('BotStatus'))
            values_update = {"$set": { "BotStatus" : bot_status}}
            st_bot.update(id_update, values_update)
    except:
        return err.e9000

    return succ.s9000
#endregion