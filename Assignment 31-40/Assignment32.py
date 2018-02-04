list1 = []
list1 = input("Input No. seprated by ',' > ")
list1 = list1.split(',')

for i in range(len(list1)-1):
    for j in range(i+1, len(list1)):
        if ( list1[j] > list1[i]):
            list1[j],list1[i] = list1[i],list1[j]

print(list1)