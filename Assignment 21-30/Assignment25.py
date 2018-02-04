string = input("Enter a string > ")
ignore = " "
res = ""

for char in string:
    if char not in ignore:
        res = res + char

print("Reverse of the string is > ")
print(res[::-2])