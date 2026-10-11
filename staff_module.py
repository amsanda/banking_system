
def staff_login(data, save_data):
    print("\n STAFF LOGIN ")
    username = input("Enter staff username: ")
    password = input("Enter staff password: ")

    # Check if username exists and password matches
    if username in data["staff"] and data["staff"][username]["password"] == password:
        print(f"\nWelcome, {username}!\n")
        staff_menu(username, data, save_data)  # Open staff menu after successful login
    else:
        print("Invalid credentials.\n")


# CREATE CUSTOMER ACCOUNT

def create_customer_account(data, save_data):
    print("\n CREATE CUSTOMER ACCOUNT ")
    customer_username = input("Enter new customer username: ")

    # Check if customer already exists
    if customer_username in data["customers"]:
        print("Customer already exists!\n")
        return
    
    # Try to get opening balance and handle invalid input
    try: 
        opening_balance = float(input("Enter opening balance: "))  # Ask for starting balance

    except ValueError: # Handle non-numeric input
        print("Invalid amount!\n")
        return

    # Add new customer details to data dictionary
    data["customers"][customer_username] = {
        "balance": opening_balance,
        "restricted": False  # New customers are unrestricted by default
    }

    save_data(data)
    print(f"Customer '{customer_username}' created with ₦{opening_balance} successfully!\n")


# DEPOSIT / CREDIT CUSTOMER ACCOUNT 

def deposit_to_customer(data, save_data):
    print("\n DEPOSIT TO CUSTOMER ACCOUNT ")
    customer_username = input("Enter customer username: ")

    if customer_username not in data["customers"]:
        print("Customer not found!\n")
        return

    if data["customers"][customer_username]["restricted"]:
        print("This customer's account is restricted. Cannot deposit.\n")
        return

    try: # Get deposit amount and handle invalid input
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("Invalid amount!\n")
        return

    # Increase customer balance
    data["customers"][customer_username]["balance"] += amount
    save_data(data)
    print(f"₦{amount} deposited to '{customer_username}' successfully!\n")


# WITHDRAW MONEY FROM CUSTOMER ACCOUNT

def withdraw_from_customer(data, save_data):
    print("\n WITHDRAW FROM CUSTOMER ACCOUNT ")
    customer_username = input("Enter customer username: ")

    if customer_username not in data["customers"]:
        print("Customer not found!\n")
        return

    # Check if account is restricted
    if data["customers"][customer_username]["restricted"]:
        print("This customer's account is restricted. Cannot withdraw.\n")
        return

    try:
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("Invalid amount!\n")
        return

    # Check sufficient funds
    if amount > data["customers"][customer_username]["balance"]:
        print("Insufficient balance!\n")
        return

    # Deduct amount
    data["customers"][customer_username]["balance"] -= amount
    save_data(data)
    print(f"₦{amount} withdrawn from '{customer_username}' successfully!\n")


# CHECK CUSTOMER BALANCE

def check_customer_balance(data):
    print("\n CHECK CUSTOMER BALANCE ")
    customer_username = input("Enter customer username: ")

    if customer_username not in data["customers"]:
        print("Customer not found!\n")
        return

    balance = data["customers"][customer_username]["balance"]
    restricted = data["customers"][customer_username]["restricted"]
    print(f"Customer: {customer_username}")
    print(f"Balance: ₦{balance}")
    print(f"Restricted: {restricted}\n")


# RESTRICT CUSTOMER ACCOUNT

def restrict_customer_account_staff(data, save_data):
    print("\n RESTRICT CUSTOMER ACCOUNT ")
    customer_username = input("Enter customer username: ")

    if customer_username not in data["customers"]:
        print("Customer not found!\n")
        return

    choice = input("Do you want to restrict this account? (yes/no): ").lower()

    if choice == "yes":
        data["customers"][customer_username]["restricted"] = True
        print(f"'{customer_username}' account restricted.\n")
    else:
        data["customers"][customer_username]["restricted"] = False
        print(f"'{customer_username}' restriction removed.\n")

    save_data(data)

def delete_customer_account(data, save_data):
    print("\n DELETE CUSTOMER ACCOUNT ")
    customer_username = input("Enter customer username to delete: ")

    # Check if customer exists
    if customer_username not in data["customers"]:
        print("Customer not found!\n")
        return

    # Confirm before deleting
    confirm = input(f"Are you sure you want to delete '{customer_username}'? (yes/no): ").lower()
    if confirm == "yes":
        del data["customers"][customer_username]  # Remove customer
        save_data(data)  # Save changes
        print(f"Customer account '{customer_username}' has been deleted successfully!\n")
    else:
        print("Deletion cancelled.\n")

def unblock_customer_account(data, save_data):
    print("\n UNBLOCK CUSTOMER ACCOUNT ")
    customer_username = input("Enter customer username to unblock: ")

    # Check if customer exists
    if customer_username not in data["customers"]:
        print("Customer not found!\n")
        return

    # Check if account is actually blocked
    if not data["customers"][customer_username].get("blocked", False):
        print(f"Customer '{customer_username}' account is not blocked.\n")
        return

    # Confirm before unblocking
    confirm = input(f"Are you sure you want to unblock '{customer_username}'? (yes/no): ").lower()
    if confirm == "yes":
        data["customers"][customer_username]["blocked"] = False
        save_data(data)
        print(f"Customer '{customer_username}' account has been successfully unblocked!\n")
    else:
        print("Unblocking cancelled.\n")

# STAFF MENU

def staff_menu(username, data, save_data):
    while True:
        print(" STAFF MENU ")
        print("1. Create Customer Account")
        print("2. Deposit to Customer Account")
        print("3. Withdraw from Customer Account")
        print("4. Check Customer Balance")
        print("5. Restrict Customer Account")
        print("6. Delete Customer Account")
        print("7. Unblock Customer Account")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_customer_account(data, save_data)
        elif choice == "2":
            deposit_to_customer(data, save_data)
        elif choice == "3":
            withdraw_from_customer(data, save_data)
        elif choice == "4":
            check_customer_balance(data)
        elif choice == "5":
            restrict_customer_account_staff(data, save_data)
        elif choice == "6":
            delete_customer_account(data, save_data)
        elif choice == "7":
            unblock_customer_account(data, save_data)
        elif choice == "8":
            print("Logging out...\n")
            break
        else:
            print("Invalid option. Try again.\n")