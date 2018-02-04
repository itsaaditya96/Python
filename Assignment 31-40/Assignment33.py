lst = [["Sofa set",20000],["Dining table",8500],["T.V. Stand",4599],["Cupboard",13920]]

item = input("Enter ITEM to be purchased > ")
ind=0

for i,sublist in enumerate(lst):
    if item in sublist:
        ind = i
    
if item in [j for i in lst for j in i]:
    quantity = int(input("Enter Quantity > "))
    if quantity > 0:
        print(quantity*lst[ind][1])
    else:
        print("Quantity must be grater then 0")
else:
    print("Item Not Available")