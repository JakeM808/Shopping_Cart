# Create an empty dictionary to store the cart data.
cart = {}

# Function to add items
def add_item(item, quantity=1, price=0):
    # If new item, add to cart
    if item not in cart:
        cart[item] = (quantity, price)
        

    
    # Else, increase the quantity of existing item
    else:
        cart[item] = (cart[item][0] + quantity, cart[item][1])

# Function to remove items
def remove_item(item, quantity=1):
    # Remove items by user input
    if item in cart:
        cart[item] = (cart[item][0] - quantity, cart[item][1])
    else:
        print('There are no cart[item]"s" in your cart')

# Function to display items and values
def view_cart():
    total = 0
    print("Items in your cart:")
    for item, tup in cart.items():
        item_total = round(tup[0] * tup[1],2)
        
        print(f"You have {tup[1]} {item} in your cart, which cost ${item_total})")
        total += item_total
        print(f"Total: ${total}")


# Function to display receipt and exit
def quit():
    print("Receipt:")
    total = 0 
    for item, (quantity, price) in cart.items():
        print(f"{item}: {quantity} x ${price}")
        total += round(quantity * price,2)
    print(f"Total: ${total}")

    cart.clear()

    
   
   

# Main program
while True:

    print("Menu:")
    print("Add item to cart")
    print("Remove item from cart")
    print("View cart")
    print("Quit")

    # Get user input
    choice = input("What would you like to do? ").title()

    # User selction add to cart
    if choice == 'Add':
        item = input("Enter the item: ")
        price = float(input("How much does one cost? "))
        quantity = int(input("Enter the quantity: "))
        add_item(item, quantity, price)
    
    # User selection remove from cart
    elif choice == 'Remove':
        item = input("Enter the item: ")
        quantity = int(input('How many would you like to remove? '))
        remove_item(item, quantity)
    # View
    elif choice == 'View':
        view_cart()
    # Quit
    elif choice == 'Quit':
        quit()
        break
    else:
        print("Invalid choice")



     