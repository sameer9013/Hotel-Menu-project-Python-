#hotel menu project 

#deline the menu of restro 
# Define the menu of the restaurant
menu = {
    "pizza": 120,
    "burger": 60,
    "kulcha": 100,
    "sandwich": 40,
    "pattie": 30,
    "roll": 70,
    "momos": 80,
    "chowmin": 130,
    "samosa": 20,
    "thali": 120,
    "paneer tikka": 150,
    "chaap": 140,
    "salad": 60,
    "cold drink 250ml": 60,
    "cold coffee": 80,
    "water": 30
}

# Greeting the customer
print("WELCOME TO SAMEER RESTRO....")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item.title()} - Rs {price}")

# Total order
total_price_of_order = 0

while True:
    # Item add
    item1 = input("Enter the item you want to order: ").strip().lower()

    # Item in menu or not
    if item1 in menu:
        total_price_of_order += menu[item1]
        print(f"Your item '{item1.title()}' added to the cart.")
    else:
        print("This item is not in the menu, try something else....")

    # Another item
    another_item = input("Do you want something else? (yes/no): ").strip().lower()
    if another_item != "yes":
        break

# Final amount
print(f"\nTotal amount you have to pay is: Rs {total_price_of_order}")
print("THANK YOU FOR VISITING SAMEER RESTRO......")



