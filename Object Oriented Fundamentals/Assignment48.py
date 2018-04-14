class Customer:
    def setcustomerid(self, customerid):
        self.customerid = customerid 
        
    def settelephoneno(self, teleno):
        self.telephoneno = teleno 
        
    def getcustomerid(self):
        return self.customerid 
    
    def gettelephoneno(self): 
        return self.telephoneno 
    
    
custobj = Customer() 
custobj.setcustomerid(1001) 
custobj.settelephoneno(9201861311) 
print("Customer Id : ", custobj.getcustomerid()) 
print("Telephone No : ", custobj.gettelephoneno())