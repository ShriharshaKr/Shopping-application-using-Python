import sys
import  uuid
# Sample databases
users = {"user1": {"password": "password123", "session_id": None},
         "admin": {"password": "adminpass", "session_id": None}}
catalog = {
    "1": {"name": "Boots", "category": "Footwear", "price": 1500},
    "2": {"name": "Jacket", "category": "Clothing", "price": 3000},
    "3": {"name": "Laptop", "category": "Electronics", "price": 50000}
}
carts = {}
categories = {"Footwear", "Clothing", "Electronics"}
def welcome():
    print("Welcome to the Demo Marketplace")
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username]["password"] == password:
        users[username]["session_id"] = str(uuid.uuid4())  # Assigning session ID
        if username == "admin":
            admin_menu()
        else:
            user_menu(username)
    else:
        print("Invalid credentials! Try again.")
        login()
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. View Products")
        print("2. View Categories")
        print("3. Add Product")
        print("4. Modify Product")
        print("5. Remove Product")
        print("6. Add Category")
        print("7. Remove Category")
        print("8. Logout")

        choice = input("Enter choice: ")
        if choice == "1":
            view_catalog()
        elif choice == "2":
            view_categories()
        elif choice == "3":
            add_product()
        elif choice == "4":
            modify_product()
        elif choice == "5":
            remove_product()
        elif choice == "6":
            add_category()
        elif choice == "7":
            remove_category()
        elif choice == "8":
            print("Logged out successfully!")
            break
        else:
            print("Invalid choice! Try again.")
def add_product():
    prod_id = input("Enter new product ID: ")
    name = input("Enter product name: ")
    category = input("Enter category: ")
    if category not in categories:
        print("Category does not exist! Add it first.")
        return
    price = int(input("Enter price: "))
    catalog[prod_id] = {"name": name, "category": category, "price": price}
    print(f"Product {name} added successfully!")
def view_categories():
    print("\nAvailable Categories:")
    for category in categories:
        print(f"- {category}")
def add_category():
    category = input("Enter new category name: ")
    categories.add(category)
    print(f"Category '{category}' added successfully!")
def remove_category():
    category = input("Enter category name to remove: ")
    if category in categories:
        categories.remove(category)
        print(f"Category '{category}' removed successfully!")
    else:
        print("Category not found!")
def modify_product():
    prod_id = input("Enter product ID to modify: ")
    if prod_id in catalog:
        name = input("Enter new name: ")
        category = input("Enter new category: ")
        if category not in categories:
            print("Category does not exist! Add it first.")
            return
        price = int(input("Enter new price: "))
        catalog[prod_id] = {"name": name, "category": category, "price": price}
        print("Product updated successfully!")
    else:
        print("Product not found!")
def remove_product():
    prod_id = input("Enter product ID to remove: ")
    if prod_id in catalog:
        del catalog[prod_id]
        print("Product removed successfully!")
    else:
        print("Product not found!")
def user_menu(username):
    while True:
        print("\nUser Menu:")
        print("1. View Catalog")
        print("2. View Cart")
        print("3. Add to Cart")
        print("4. Remove from Cart")
        print("5. Checkout")
        print("6. Logout")

        choice = input("Enter choice: ")
        if choice == "1":
            view_catalog()
        elif choice == "2":
            view_cart(username)
        elif choice == "3":
            add_to_cart(username)
        elif choice == "4":
            remove_from_cart(username)
        elif choice == "5":
            checkout(username)
        elif choice == "6":
            print("Logged out successfully!")
            break
        else:
            print("Invalid choice! Try again.")
def view_cart(username):
    if username in carts and carts[username]:
        print("\nYour Cart:")
        for pid in carts[username]:
            details = catalog[pid]
            print(f"ID: {pid}, Name: {details['name']}, Category: {details['category']}, Price: {details['price']}")
    else:
        print("Your cart is empty.")
def add_to_cart(username):
    if username not in carts:
        carts[username] = []
    prod_id = input("Enter product ID to add to cart: ")
    if prod_id in catalog:
        carts[username].append(prod_id)
        print("Product added to cart!")
    else:
        print("Invalid product ID!")
def remove_from_cart(username):
    if username in carts and carts[username]:
        prod_id = input("Enter product ID to remove from cart: ")
        if prod_id in carts[username]:
            carts[username].remove(prod_id)
            print("Product removed from cart!")
        else:
            print("Product not found in cart!")
    else:
        print("Cart is empty!")

def checkout(username):
    if username in carts and carts[username]:
        total = sum(catalog[pid]["price"] for pid in carts[username])
        print(f"Total amount: {total}")
        payment_method = input("Select payment method (Net banking/PayPal/UPI): ")
        print(f"Your order is successfully placed via {payment_method}!")
        carts[username] = []
    else:
        print("Cart is empty!")

def view_catalog():
    print("\nProduct Catalog:")
    for pid, details in catalog.items():
        print(f"ID: {pid}, Name: {details['name']}, Category: {details['category']}, Price: {details['price']}")

if __name__ == "__main__":
    welcome()
    login()
