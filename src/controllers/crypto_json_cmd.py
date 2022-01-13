def get_real_account(in_json):
    try:
        return in_json['RealAccount']
    except:
        return 0