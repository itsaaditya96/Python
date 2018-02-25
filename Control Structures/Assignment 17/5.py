amount = 100.0
intrest = 0.0
months = 1
while months < 6:
    intrest = amount * 0.2
    amount = amount + intrest
    months += 1
    print(amount)