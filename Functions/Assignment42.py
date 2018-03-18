custid = [1001,1002,1003,1004,1005]

x = input("Enter Customer Id > ")

if type(x) is str:
    try:
        print("The Entry is", x)
        custid[3] = int(x)
        #break
    finally:
        print("Sorry!, Entry Can not be String")

try:
    print(custid[5])
except IndexError:
    print("\nTrying to display unavailable value")
    
print("\nValues are > ", custid)