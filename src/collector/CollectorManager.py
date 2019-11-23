import tushare as ts
import MySQLdb

# CollectorManager's function 
# 1.manages all collector
# 2.link to database and store stock data to database 
class CollectorManager:

    #public:    
    def __init__(self, param):
        self.db = 

    # init older tushare
    def initTushare(self, token):
        self.ts = ts.set_token(token)

    # init Tushare Pro
    def initTusharePro(token)
        return 0    

    # read data from internet
    def updateAll(self):
        self.updateStockList()
        self.updateStockBasic()
        self.updateBalance()
        self.updateCashFlow()
        self.updateIncome()

    #private
    def store(self,data):
        return 0
    
    def merge(data1,data2):
        return 

    def updateStockList():
        data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,market,list_status,list_date,is_hs')
        store(data)

    #TODO
    def updateStockBasic(self):
        return 0
    def updateBalance(self);
        return 0
    def updateIncome(self):
        return 0
    def updateCashFlow(self):
        return 0
