# ================================================================
# STEP 1: Load or Initialize Data Storage
# ================================================================
# We will store all system data (managers, staff, and customers)
# inside a JSON file to make it persistent between sessions.
import json  # Import json module to handle saving and loading data
from staff_module import staff_login  # Import staff login function

try:
    # Try to open and load existing data from the JSON file
    with open("bank_data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    # If the file doesn’t exist, initialize with default structure
    data = {
        "managers": {
            "admin": {"password": "admin123"}  # Default manager credentials
        },
        "staff": {},       # Empty dictionary for staff accounts
        "customers": {}    # Empty dictionary for customer accounts
    }

# ================================================================
# STEP 2: Save Data Function
# ================================================================
# This function saves any modifications to our data file.

def save_data():
    """Save the current banking data to the JSON file."""
    with open("bank_data.json", "w") as file:
        json.dump(data, file, indent=4)  # Write data with indentation
    print("✅ Data saved successfully!\n")


# ================================================================
# STEP 3: Manager Login Function
# ================================================================
# This function handles login for managers using username and password.

def manager_login():
    """Allow a manager to log in using username and password."""
    print("\n==== MANAGER LOGIN ====")
    username = input("Enter manager username: ")
    password = input("Enter manager password: ")

    # Validate login credentials
    if username in data["managers"] and data["managers"][username]["password"] == password:
        print(f"\n✅ Welcome, {username}!\n")
        manager_menu(username)
    else:
        print("❌ Invalid credentials. Try again.\n")


# ================================================================
# STEP 4: Add Staff Function
# ================================================================

def add_staff():
    """Allow manager to add a new staff member."""
    print("\n==== ADD NEW STAFF ====")
    staff_username = input("Enter new staff username: ")

    # Check if username already exists
    if staff_username in data["staff"]:
        print("❌ Staff username already exists!\n")
        return

    staff_password = input("Enter staff password: ")

    data["staff"][staff_username] = {
        "password": staff_password
    }

    save_data()
    print(f"✅ Staff '{staff_username}' added successfully!\n")


# ================================================================
# STEP 5: View All Staff Function
# ================================================================

def view_all_staff():
    """Display all staff members in the system."""
    print("\n==== ALL STAFF MEMBERS ====")

    if not data["staff"]:
        print("No staff found.\n")
        return

    for username, details in data["staff"].items():
        print(f"👤 Username: {username} | Password: {details['password']}")

    print("\n✅ End of staff list.\n")


# ================================================================
# STEP 6: Remove Staff Function
# ================================================================

def remove_staff():
    """Allow manager to remove an existing staff member."""
    print("\n==== REMOVE STAFF ====")
    staff_username = input("Enter the staff username to remove: ")

    if staff_username not in data["staff"]:
        print("❌ No such staff found!\n")
        return

    confirm = input(f"Are you sure you want to remove '{staff_username}'? (yes/no): ").lower()

    if confirm == "yes":
        del data["staff"][staff_username]
        save_data()
        print(f"✅ Staff '{staff_username}' has been removed successfully!\n")
    else:
        print("❌ Action cancelled.\n")


# ================================================================
# STEP 7: Change Staff Password Function
# ================================================================

def change_staff_password():
    """Allow manager to change an existing staff member's password."""
    print("\n==== CHANGE STAFF PASSWORD ====")
    staff_username = input("Enter staff username: ")

    if staff_username not in data["staff"]:
        print("❌ Staff username not found!\n")
        return

    new_password = input("Enter new password for staff: ")
    confirm_password = input("Confirm new password: ")

    if new_password != confirm_password:
        print("❌ Passwords do not match!\n")
        return

    data["staff"][staff_username]["password"] = new_password
    save_data()
    print(f"✅ Password for '{staff_username}' has been changed successfully!\n")


# ================================================================
# STEP 8: Restrict Customer Account Function
# ================================================================

def restrict_customer_account():
    """Allow manager to restrict a customer's account."""
    print("\n==== RESTRICT CUSTOMER ACCOUNT ====")
    customer_username = input("Enter customer username: ")

    if customer_username not in data["customers"]:
        print("❌ Customer not found!\n")
        return

    data["customers"][customer_username]["restricted"] = True
    save_data()
    print(f"✅ Customer '{customer_username}' account has been restricted.\n")


# ================================================================
# STEP 9: View All Customers Function
# ================================================================

def view_all_customers():
    """Display all customers with their details."""
    print("\n==== ALL CUSTOMERS ====")

    if not data["customers"]:
        print("No customers found.\n")
        return

    for username, details in data["customers"].items():
        restricted = "🔒 Restricted" if details.get("restricted") else "✅ Active"
        print(f"👤 Username: {username} | Balance: ₦{details.get('balance', 0)} | Status: {restricted}")

    print("\n✅ End of customer list.\n")


# ================================================================
# STEP 10: Update Customer Balance Function
# ================================================================

def update_customer_balance():
    """Allow manager to manually update a customer's balance."""
    print("\n==== UPDATE CUSTOMER BALANCE ====")
    customer_username = input("Enter customer username: ")

    if customer_username not in data["customers"]:
        print("❌ Customer not found!\n")
        return

    try:
        new_balance = float(input("Enter new balance amount: "))
        data["customers"][customer_username]["balance"] = new_balance
        save_data()
        print(f"✅ Balance for '{customer_username}' updated successfully!\n")
    except ValueError:
        print("❌ Invalid amount entered!\n")


# ================================================================
# STEP 11: Manager Menu
# ================================================================

def manager_menu(username):
    """Display the manager's options after successful login."""
    while True:
        print("==== MANAGER MENU ====")
        print("1. Add Staff")
        print("2. View All Staff")
        print("3. Remove Staff")
        print("4. Change Staff Password")
        print("5. Restrict Customer Account")
        print("6. View All Customers")
        print("7. Update Customer Balance")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_staff()
        elif choice == "2":
            view_all_staff()
        elif choice == "3":
            remove_staff()
        elif choice == "4":
            change_staff_password()
        elif choice == "5":
            restrict_customer_account()
        elif choice == "6":
            view_all_customers()
        elif choice == "7":
            update_customer_balance()
        elif choice == "8":
            print("👋 Logging out...\n")
            break
        else:
            print("⚠️ Invalid option. Try again.\n")


# ================================================================
# STEP 12: Main Menu (Entry Point)
# ================================================================

def main_menu():
    """Main entry point for the banking system."""
    while True:
        print("==== WELCOME TO DEVELOPERS BANK ====")
        print("1. Manager Login")
        print("2. Staff Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager_login()
        elif choice == "2":
            staff_login()  # ✅ This now calls the function in staff_module.py
        elif choice == "3":
            print("👋 Goodbye! Have a nice day.\n")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")



# ================================================================
# STEP 13: Run the Program
# ================================================================

if __name__ == "__main__":
    main_menu()

# ================================================================
# STAFF MODULE
# ================================================================
# This file handles everything a staff member can do in the system.
# It imports shared data and save_data() from the main banking system.
# ================================================================

from banking_system import data, save_data  # Import shared data and save function


# ================================================================
# STAFF LOGIN FUNCTION
# ================================================================

def staff_login():
    """Allow a staff member to log in using their username and password."""
    print("\n==== STAFF LOGIN ====")
    username = input("Enter staff username: ")
    password = input("Enter staff password: ")

    # Verify login
    if username in data["staff"] and data["staff"][username]["password"] == password:
        print(f"\n✅ Welcome, {username}!\n")
        staff_menu(username)  # Open staff menu
    else:
        print("❌ Invalid credentials. Try again.\n")


# ================================================================
# CREATE CUSTOMER ACCOUNT
# ================================================================

def create_customer_account():
    """Allow staff to create a new customer account."""
    print("\n==== CREATE CUSTOMER ACCOUNT ====")
    customer_username = input("Enter customer username: ")

    # Check if customer already exists
    if customer_username in data["customers"]:
        print("❌ Customer already exists!\n")
        return

    try:
        opening_balance = float(input("Enter opening balance: "))
    except ValueError:
        print("❌ Invalid amount entered!\n")
        return

    # Initialize new customer details
    data["customers"][customer_username] = {
        "balance": opening_balance,
        "restricted": False
    }

    save_data()
    print(f"✅ Customer account '{customer_username}' created successfully with ₦{opening_balance}\n")


# ================================================================
# DEPOSIT TO CUSTOMER ACCOUNT
# ================================================================

def deposit_to_customer():
    """Allow staff to deposit money into a customer's account."""
    print("\n==== DEPOSIT TO CUSTOMER ACCOUNT ====")
    customer_username = input("Enter customer username: ")

    if customer_username not in data["customers"]:
        print("❌ Customer not found!\n")
        return

    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("❌ Amount must be positive!\n")
            return
    except ValueError:
        print("❌ Invalid amount entered!\n")
        return

    data["customers"][customer_username]["balance"] += amount
    save_data()
    print(f"✅ Deposited ₦{amount} to '{customer_username}'. New balance: ₦{data['customers'][customer_username]['balance']}\n")


# ================================================================
# WITHDRAW FROM CUSTOMER ACCOUNT
# ================================================================

def withdraw_from_customer():
    """Allow staff to withdraw money from a customer's account."""
    print("\n==== WITHDRAW FROM CUSTOMER ACCOUNT ====")
    customer_username = input("Enter customer username: ")

    if customer_username not in data["customers"]:
        print("❌ Customer not found!\n")
        return

    if data["customers"][customer_username].get("restricted", False):
        print("🚫 This account is restricted. Withdrawal not allowed!\n")
        return

    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("❌ Amount must be positive!\n")
            return
    except ValueError:
        print("❌ Invalid amount entered!\n")
        return

    if data["customers"][customer_username]["balance"] < amount:
        print("❌ Insufficient funds!\n")
        return

    data["customers"][customer_username]["balance"] -= amount
    save_data()
    print(f"✅ Withdrawn ₦{amount} from '{customer_username}'. Remaining balance: ₦{data['customers'][customer_username]['balance']}\n")


# ================================================================
# CHECK CUSTOMER BALANCE
# ================================================================

def check_customer_balance():
    """Allow staff to check a customer's account balance."""
    print("\n==== CHECK CUSTOMER BALANCE ====")
    customer_username = input("Enter customer username: ")

    if customer_username not in data["customers"]:
        print("❌ Customer not found!\n")
        return

    balance = data["customers"][customer_username]["balance"]
    restricted = data["customers"][customer_username].get("restricted", False)
    status = "🔒 Restricted" if restricted else "✅ Active"

    print(f"👤 Customer: {customer_username}\n💰 Balance: ₦{balance}\nStatus: {status}\n")


# ================================================================
# RESTRICT CUSTOMER ACCOUNT
# ================================================================

def restrict_customer_by_staff():
    """Allow staff to restrict a customer's account."""
    print("\n==== RESTRICT CUSTOMER ACCOUNT ====")
    customer_username = input("Enter customer username: ")

    if customer_username not in data["customers"]:
        print("❌ Customer not found!\n")
        return

    data["customers"][customer_username]["restricted"] = True
    save_data()
    print(f"✅ Customer '{customer_username}' account has been restricted by staff.\n")


# ================================================================
# STAFF MENU
# ================================================================

def staff_menu(username):
    """Display the staff's options after successful login."""
    while True:
        print("==== STAFF MENU ====")
        print("1. Create Customer Account")
        print("2. Deposit to Customer Account")
        print("3. Withdraw from Customer Account")
        print("4. Check Customer Balance")
        print("5. Restrict Customer Account")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_customer_account()
        elif choice == "2":
            deposit_to_customer()
        elif choice == "3":
            withdraw_from_customer()
        elif choice == "4":
            check_customer_balance()
        elif choice == "5":
            restrict_customer_by_staff()
        elif choice == "6":
            print("👋 Logging out...\n")
            break
        else:
            print("⚠️ Invalid option. Try again.\n")
