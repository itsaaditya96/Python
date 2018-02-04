bill_id = 1001
customer_id=101
bill_amount=1200.0
discounted_bill_amount=0.0
discount = 0
print("Bill Id:%d"%bill_id)
print("Customer Id:%d"%customer_id)
print("Bill Amount:Rs. %f"%bill_amount)
if bill_amount >= 1000:
    discount=5
elif bill_amount >=500:
    discount=2
else:
    discount=1
discounted_bill_amount = bill_amount - bill_amount * discount/100
print("Discounted Bill Amount:Rs. %f"%discounted_bill_amount)