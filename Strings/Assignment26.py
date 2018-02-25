string = "ABaBCbGc"
string1 = string.upper();

dic = {}

for char in string1:  
    dic[char] = 0  
  
for char in string1:  
    dic[char]+= 1  
  
for char, count in dic.items():  
    if count > 0 and char != ' ':  
        print ("%d%c" % (count, char))