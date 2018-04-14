class Customer: 
    def __init__(self, customerid, telephoneno, customername): 
        self.__customerid=customerid 
        self.__customername=customername 
        self.__telephoneno=telephoneno 
        
    def setcustomerid(self, id): 
        self.__customerid = id 
        
    def setcustomername(self, customername): 
        self.__customername = customername 
        
    def settelephoneno(self, teleno): 
        self.__telephoneno = teleno 
        
    def getcustomerid(self): 
        return self.__customerid 
    
    def gettelephoneno(self): 
        return self.__telephoneno 
    
    def getcustomername(self):
        return self.__customername
    
    def validatecustomername(self): 
        if(len(self.__customername)>=3 and len(self.__customername) <=20): 
            return True 
        
        else: 
            return False 
        
telephoneno=[9201861311, 9201861321, 9201661311] 
custobj = Customer(1001, telephoneno, "Kevin") 
if(custobj.validatecustomername()): 
    print("Customer Id : ", custobj.getcustomerid()) 
    temp = custobj.gettelephoneno() 
    print("Telephone Nos : ", temp[0], ",", temp[1], ",", temp[2]) 
    print("Customer Name : ", custobj.getcustomername()) 
else: 
    print("Invalid customer name. Customer name must be between 3 and 20 characters")