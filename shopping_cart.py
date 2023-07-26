# Create an empty dictionary to store the cart data.
cart = {}

# Function to add items
def add_item(item, quantity, price):
    # If new item, add to cart
    if item not in cart:
        cart[item] = quantity
    # Else, increase the quantity of existing item
    else:
        cart[item] += quantity

# Function to remove items
def remove_item(item):
    # Remove items by user input
    if item in cart:
        cart[item] -= quantity
    # If quantity of item <= 0, delete item
    if cart[item] <= 0:
        del cart[item]

# Function to display items and values
def view_cart():
    print("Items in your cart:")
    for item, quantity in cart.items():
        print(f"{item}: {quantity} x ${item.price}")


# Function to display receipt and exit
def quit():
    print("Receipt:")
    total = 0 
    for item, quantity in cart.items():
        print(f"{item}: {quantity} x ${item.price}")
        total += quantity * item.price
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
    choice = input("What would you like to do? ")

    # User selction add to cart
    if choice == 'Add':
        item = input("Enter the item: ")
        price = float(input("How much does one cost? "))
        quantity = int(input("Enter the quantity: "))
        add_item(item, quantity, price)
    
    # User selection remove from cart
    elif choice == 'Remove':
        item = input("Enter the item: ")
        quantity = input('How many would you like to remove? ')
        remove_item(item)
    # Vew
    elif choice == 'View':
        view_cart()
    # Quit
    elif choice == 'Quit':
        quit()
        break
    else:
        print("Invalid choice")



     