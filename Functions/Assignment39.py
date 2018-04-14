def baggage_check(amount):
    if amount in range(0,40):
        return True
    else:
        return False

def immigration_check (expiry_year):
    if expiry_year in range(2001,2025):
        return True
    else:
        return False

def security(status):
    return status
def traveler():
    traveler_id = 1001
    traveler_name = "Jim"
    baggageAmount = 35
    expiryDate = 2019
    nocStatus = True
    
    if baggage_check(baggageAmount) is True & immigration_check(expiryDate) is True & security(nocStatus) is True:
        print(traveler_id,traveler_name,"\nAllowed to fly!")
    else:
        print(traveler_id,traveler_name,"\nDetain Traveller for Re-checking!")

traveler()
