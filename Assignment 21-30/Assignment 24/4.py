punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = input("Enter a string > ")

nopunctuation = ""
for char in string:
    if char not in punctuations:
        nopunctuation = nopunctuation + char

print(nopunctuation)