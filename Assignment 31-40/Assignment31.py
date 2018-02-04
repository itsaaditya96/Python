a = 0
b = 1
n=int(input("Enter n > "))
list1 = list([a,b])

for i in range(0,n-2):
    c=a+b
    a=b
    b=c
    list1.insert(i+2, c)
    
print(list1)
