bill_id = 1001
customer_id=101
bill_amount=200.0
discounted_bill_amount=0.0
print("Bill Id:%d"%bill_id)
print("Customer Id:%d"%customer_id)
print("Bill Amount:Rs. %f"%bill_amount)
if ((customer_id > 100) and (customer_id <=1000)) is True:
    if bill_amount >= 500:
        discounted_bill_amount = bill_amount-bill_amount *10/100
        print("Discounted Bill Amount:Rs. %f" %discounted_bill_amount)
    else:
        print("No Discount")
else:
        print("Invalid Customer id,customer id must between 101 and 1000")