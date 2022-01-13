from ..db.tbl import virt_wallet
from ..db.tbl.DT import bot as dt_bot
from ..db.tbl.GT import bot as gt_bot
from ..db.tbl.ST import bot as st_bot
from ..controllers import select

tbl_dt = dt_bot.get_tbl()
tbl_st = st_bot.get_tbl()
tbl_gt = gt_bot.get_tbl()

tbl_wallet = virt_wallet.get_tbl()

def get_balances():
    list_transaction = tbl_wallet.find()
    result = {}
    for transaction in list_transaction:
        sum = 0
        try:
            sum = result[transaction['CryptoName']]
        except:
            None
        result[transaction['CryptoName']] = sum + transaction['Amount']

    return result

def get_gain():
    list_transaction = tbl_wallet.find({"CryptoName": 'USDT', "Descption": {"$ne": 'Init balance'}, "Amount": {"$gte": 0} })
    list_crypto = tbl_wallet.find({"CryptoName": 'BTC', "Descption": {"$ne": 'Init balance'}, "Amount": {"$gte": 0}})
    list_bot1 = tbl_dt.find({"BotStatus": 0})
    list_bot2 = tbl_st.find({"BotStatus": 0})
    list_bot3 = tbl_gt.find({"BotStatus": 0})

    result = {}
    result['Gain'] = select.sum(list_transaction, 'Amount')
    result['CryptoSum'] = select.sum(list_crypto, 'Amount')

    result['Result'] = select.sum(list_bot1, 'BotAmount')
    result['Result'] = result['Result'] + select.sum(list_bot2, 'BotAmount')
    result['Result'] = result['Result'] + select.sum(list_bot3, 'BotAmount')

    result['Crypto'] = select.sum(tbl_dt.find({"BotStatus": 1}), 'CryptoAmount')
    result['Crypto'] = result['Crypto'] + select.sum(tbl_st.find({"BotStatus": 1}), 'CryptoAmount')
    result['Crypto'] = result['Crypto'] + select.sum(tbl_gt.find({"BotStatus": 1}), 'CryptoAmount')

    result['FinalResult'] = result['Gain'] - result['Result']
    result['CryptoSobra'] = result['CryptoSum'] - result['Crypto']

    return result