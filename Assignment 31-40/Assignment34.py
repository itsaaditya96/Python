fruits = {"apple", "orange", "banana", "apple", "pear", "papaya", "papaya"}
fruit_basket = {"apple", "banana", "grapes", "mango", "kiwi"}

print("1.",fruits)
print("2.",fruits & fruit_basket)
print("3.",fruits | fruit_basket)
print("4.",fruits - fruit_basket)
print("5.",fruits ^ fruit_basket)
print("6.",len(fruit_basket))
print("7.","pear" in fruits)
print("8.","pear" not in fruit_basket)
print("9.",fruits.issubset(fruit_basket))
print("10.",fruits.issuperset(fruit_basket))
print("11.",fruit_basket.copy())
