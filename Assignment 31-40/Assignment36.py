customer_details = { 1001 : "John", 1004 : "Jill", 1005: "Joe", 1003 : "Jack" }

print("1.",customer_details)

print("2.",len(customer_details))

print("3.",sorted(customer_details.values()))

del(customer_details[1005]) 
print("4.",customer_details)

customer_details[1003] = "Mary" 
print("5.",customer_details)

print("6.",1002 in customer_details)
