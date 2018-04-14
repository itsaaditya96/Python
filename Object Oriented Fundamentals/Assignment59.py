class PrintDetails: 
    def printheader(self, c, no=1): 
        print(c*no) 
        
class PurchaseBill: 
    def __init__(self, bid, billamount): 
        self.__billid = bid 
        self.__billamount = billamount 
        
    def getbillid(self): 
        return self.__billid 
    
    def getbillamount(self): 
        return self.__billamount 
    
    def calculatebill(self, mode, processcharge): 
        if(mode=="Credit"): 
            self.__billamount = self.__billamount + (self.__billamount * processcharge/100) 
            
    def displaybill(self): 
        objprint = PrintDetails() 
        objprint.printheader("-", 80) 
        objprint.printheader(" Easy Shop Retail Store Bill ") 
        objprint.printheader("-", 80) 
        print("Bill Id: ", self.__billid) 
        print("Final amount to be paid: Rs.", self.__billamount)
        objprint.printheader("-", 80) 
        objprint.printheader(" Thank You!!! ") 
        objprint.printheader("-", 80) 
        
objpur = PurchaseBill(101, 1055.0) 
objpur.calculatebill("Credit", 10.5) 
objpur.displaybill()