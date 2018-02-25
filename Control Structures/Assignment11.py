
unitprice=int(input("Enter price: "))
quantity=int(input("Enter quantity: "))
amount=quantity*unitprice
a1=amount*(2/100)
a2=amount*(1/100)
b1=amount-a1
b2=amount-a2
print("Bill amount:",amount)
if(amount >= 500):
    print("Your discounted price is:",b1)
else:
    print("Your discounted price is:",b2)