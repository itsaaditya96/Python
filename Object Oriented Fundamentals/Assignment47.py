class Customer:
    def setcustomerid(self, id1):
        self.__customerid = id1
        
    def settelephoneno(self, teleno):
        self.__telephoneno = teleno 
        
    def getcustomerid(self):
        return self.__customerid 
    
    def gettelephoneno(self):
        return self.__telephoneno 
    
custobj = Customer() 
custobj.setcustomerid(1001,)
custobj.settelephoneno(9201861311) 
print("Customer Id : ", custobj.getcustomerid()) 
print("Telephone No : ", custobj.gettelephoneno())