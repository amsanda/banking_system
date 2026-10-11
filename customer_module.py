def customer_login(data, save_data):
    print("\n CUSTOMER LOGIN ")
    username = input("Enter customer username: ")

    # Verify if customer exists
    if username not in data["customers"]:
        print("Customer not found.\n")
        return
    
    # ensure blocked key exists
    if "blocked" not in data["customers"][username]:
        data["customers"][username]["blocked"] = False
        save_data(data)

    # Check if blocked
    if data["customers"][username]["blocked"]:
        print("Your account is currently blocked. Contact the bank.\n")
        return

    print(f"Welcome, {username}!\n")
    customer_menu(username, data, save_data)

# CHECK BALANCE

def check_balance(username, data):
    """Allow customer to check their account balance."""
    balance = data["customers"][username]["balance"]
    print(f"\n Your current balance is: ₦{balance}\n")

#  TRANSFER MONEY

def transfer_money(username, data, save_data):
    """Allow customer to transfer money to another customer."""
    print("\n=== TRANSFER MONEY ====")
    receiver = input("Enter recipient username: ")

    # Check if receiver exists
    if receiver not in data["customers"]:
        print(" Recipient not found!\n")
        return

    # Check if receiver is not the same as sender
    if receiver == username:
        print(" You cannot transfer money to yourself!\n")
        return

    # Check if sender or receiver is blocked
    if data["customers"][username]["blocked"]:
        print("Your account is blocked — transfer denied.\n")
        return
    if data["customers"][receiver]["blocked"]:
        print("Recipient account is blocked.\n")
        return

    # Get transfer amount
    try:
        amount = float(input("Enter amount to transfer: "))
    except ValueError:
        print("Invalid amount entered!\n")
        return

    # Check for sufficient balance
    if amount > data["customers"][username]["balance"]:
        print("Insufficient funds!\n")
        return

    # Perform transfer
    data["customers"][username]["balance"] -= amount
    data["customers"][receiver]["balance"] += amount
    save_data(data)
    print(f"₦{amount} transferred successfully to '{receiver}'!\n")

# BLOCK OWN ACCOUNT

def block_account(username, data, save_data):
    """Allow customer to block (deactivate) their own account."""
    print("\n==== BLOCK ACCOUNT ====")
    confirm = input("Are you sure you want to block your account? (yes/no): ").lower()

    if confirm == "yes":
        data["customers"][username]["blocked"] = True
        save_data(data)
        print("Your account has been blocked. Contact bank staff to reactivate it.\n")
    else:
        print("Action cancelled. Account not blocked.\n")

# CUSTOMER MENU

def customer_menu(username, data, save_data):
    """Display menu options for logged-in customers."""
    while True:
        print(" CUSTOMER MENU ")
        print("1. Check Account Balance")
        print("2. Transfer Money")
        print("3. Block My Account")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(username, data)
        elif choice == "2":
            transfer_money(username, data, save_data)
        elif choice == "3":
            block_account(username, data, save_data)
            break  # Automatically log out after blocking
        elif choice == "4":
            print(" Logging out...\n")
            break
        else:
            print("Invalid option. Try again.\n")
