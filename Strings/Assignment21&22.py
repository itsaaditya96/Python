bill_id = input("Please enter Bill id > ") 
customer_id = input("Please enter Customer id > ") 
bill_amount = input("Please enter bill Amount > ") 
customer_name = input("Please enter Customer Name > ") 

if ((len(customer_name) >= 3) and (len(customer_name) <= 20)) is True: 
    print("Bill Id: ",bill_id) 
    print("Customer Id: ",customer_id) 
    print("Bill Amount:Rs. ",bill_amount) 
    print("Customer Name: ",customer_name) 
else: 
    print("Invalid customer name. Customer name must be between 3 and 20 characters");
