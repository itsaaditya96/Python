item_price = [1050, 2200, 8575, 485, 234, 150, 399] 
def price_max(item_price): 
    print("Price of Costliest item in the Retail Store: ",max(item_price)) 

def average_price(item_price): 
    total_price = 0 
    for i in item_price: 
        total_price += i 
    average_price = total_price/len(item_price) 
    print("Average Price of items in the Retail Store: ",average_price)

def display_sorted_price(item_price): 
    item_price.sort() 
    print("Item Price List in increasing order: ",item_price) 

price_max(item_price) 
average_price(item_price) 
display_sorted_price(item_price)