from .. import create_db

db = create_db.Transaction()

def get_tbl():
    return db.TBLTransaction