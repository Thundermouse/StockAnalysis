import MySQLdb

class CollectorBase:
    def __init__(self, DBhandle):
        self.sqlHandle = DBhandle
    
    
