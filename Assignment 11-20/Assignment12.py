bill_id = 1001
customer_id=101
bill_amount=200.0
discounted_bill_amount=0.0
print("Bill Id:%d"%bill_id)
print("Customer Id:%d"%customer_id)
print("Bill Amount:Rs. %f"%bill_amount)
if bill_amount>200:
    discounted_bill_amount=bill_amount - bill_amount*2/100
else:
    discounted_bill_amount=bill_amount-bill_amount*1/100
    print("Discounted Bill Amount:Rs.%f"%discounted_bill_amount)