class Customer: 
    counter = 1000 
    def __init__(self): 
        Customer.counter = Customer.counter+1 
        self.__customerid=Customer.counter 
        
    def setcustomerid(self, cid): 
        self.__customerid=cid 
        
    def getcustomerid(self): 
        return self.__customerid 
    
    @staticmethod 
    def totalcustomers(): 
        return Customer.counter-1000 
    
objcust = Customer()     
print("Customer Id: ", objcust.getcustomerid()) 

objcust2 = Customer() 
print("Customer Id: ", objcust2.getcustomerid()) 
print("Total Customers: ", objcust.totalcustomers()) 
print("Total Customers: ", objcust2.totalcustomers()) 
print("Total Customers: ", Customer.totalcustomers())