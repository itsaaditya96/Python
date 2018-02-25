stri = input("Enter a String > ")
count=0

for i in stri:
    if(i.isupper()):
        count = count + 1
print("There are",count,"Uppercase Letter in Entered String.")
