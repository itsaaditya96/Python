class Address: 
    def __init__(self, addressline, city, state, zip1): 
        self.__addressline = addressline 
        self.__city=city 
        self.__state=state 
        self.__zip=zip1
        
    def setaddressline(self, address): 
        self.__addressLine = address 
        
    def getaddressline(self): 
        return self.__addressline 
    
    def setcity(self, city): 
        self.__city = city 
        
    def getcity(self): 
        return self.__city
    
    def setstate(self, state): 
        self.__state = state 
        
    def getstate(self): 
        return self.__state 
    
    def setzip(self, zip1): 
        self.__zip = zip1 
        
    def getzip(self): 
        return self.__zip 
    
class Customer: 
    def __init__(self, cid, address): 
        self.__customerid = cid 
        self.__address = address 
        
    def getcustomerid(self): 
        return self.__customerid 
    
    def getaddress(self): 
        return self.__address 
    
objaddress = Address("No.333,Oak street", "Strathfield", "New South Wales", "570018") 
objcust = Customer(1001, objaddress) 
print("Customer Id:", objcust.getcustomerid()) 
address = objcust.getaddress() 
print("Customer Address: ", address.getaddressline(), ",", address.getcity(), ",", address.getstate(), ",", address.getzip())