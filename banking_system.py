from data_manager import load_data, save_data
from staff_module import staff_login
from customer_module import customer_login 

# Load data at the start 
data = load_data() 


# MANAGER FUNCTIONS

def manager_login(data, save_data):
    """Manager login that forwards to manager_menu with data and save_data."""
    print("\n MANAGER LOGIN ")
    username = input("Enter manager username: ")
    password = input("Enter manager password: ")

    if username in data["managers"] and data["managers"][username]["password"] == password:
        print(f"\n Welcome, {username}!\n")
        manager_menu(username, data, save_data)   
    else:
        print("Invalid manager credentials!\n")

# Add New Staff

def add_staff(data, save_data):
    """Add a new staff member """
    print("\n ADD NEW STAFF")

    # Ask for username and validate (no empty username)
    username = input("Enter staff username: ").strip()
    if not username:
        print("Username cannot be empty. Please try again.\n")
        return  

    # Ask for password and validate (no empty password)
    password = input("Enter staff password: ").strip()
    if not password:
        print("Password cannot be empty. Please try again.\n")
        return  

    # Check if staff already exists
    if username in data["staff"]:
        print(" Staff already exists!\n")
        return

    # Add staff and save
    data["staff"][username] = {"password": password}
    save_data(data)
    print(f" Staff '{username}' added successfully!\n")

# View All Staff

def view_all_staff():
    print("\n ALL STAFF MEMBERS ")
    if not data["staff"]:
        print("No staff found.\n")
        return
    for username, details in data["staff"].items():
        print(f"{username} | Password: {details['password']}")
    print()


# Remove Staff

def remove_staff():
    print("\n REMOVE STAFF ")
    staff_username = input("Enter staff username to remove: ")

    if staff_username not in data["staff"]:
        print(" No such staff!\n")
        return

    confirm = input(f"Are you sure you want to remove '{staff_username}'? (yes/no): ").lower()
    if confirm == "yes":
        del data["staff"][staff_username]
        save_data(data)
        print(f"'{staff_username}' removed successfully!\n")
    else:
        print(" Action cancelled.\n")


# Change Staff Password

def change_staff_password():
    print("\n CHANGE STAFF PASSWORD ")
    staff_username = input("Enter staff username: ")

    if staff_username not in data["staff"]:
        print("Staff not found!\n")
        return

    new_password = input("Enter new password: ")
    confirm_password = input("Confirm new password: ")

    if new_password != confirm_password:
        print("Passwords do not match!\n")
        return

    data["staff"][staff_username]["password"] = new_password
    save_data(data)
    print(f"Password for '{staff_username}' updated successfully!\n")


# Restrict Customer Account

def restrict_customer_account():
    print("\n RESTRICT CUSTOMER ACCOUNT ")
    customer_username = input("Enter customer username: ")

    if customer_username not in data["customers"]:
        print(" Customer not found!\n")
        return

    restriction = input("Restrict customer? (yes/no): ").lower()
    if restriction == "yes":
        data["customers"][customer_username]["restricted"] = True
        print(f" '{customer_username}' account restricted.\n")
    else:
        data["customers"][customer_username]["restricted"] = False
        print(f"'{customer_username}' restriction removed.\n")

    save_data(data)


# View All Customers

def view_all_customers():
    print("\n ALL CUSTOMERS ")
    if not data["customers"]:
        print("No customers available.\n")
        return
    for username, info in data["customers"].items():
        print(f"{username} | Balance: ₦{info['balance']} | Restricted: {info['restricted']}")
    print()


#  Update Customer Balance

def update_customer_balance():
    print("\n UPDATE CUSTOMER BALANCE ")
    customer_username = input("Enter customer username: ")

    if customer_username not in data["customers"]:
        print("Customer not found!\n")
        return

    try:
        new_balance = float(input("Enter new balance: "))
    except ValueError:
        print("Invalid amount!\n")
        return

    data["customers"][customer_username]["balance"] = new_balance
    save_data(data)
    print(f"Balance for '{customer_username}' updated successfully!\n")


# MANAGER MENU

def manager_menu(username, data, save_data):
    """Display the full manager menu (receives data and save_data)."""
    while True:
        print("MANAGER MENU ")
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
            add_staff(data, save_data)            
        elif choice == "2":
            view_all_staff(data)                  
        elif choice == "3":
            remove_staff(data, save_data)         
        elif choice == "4":
            change_staff_password(data, save_data)
        elif choice == "5":
            restrict_customer_account(data, save_data)
        elif choice == "6":
            view_all_customers(data)
        elif choice == "7":
            update_customer_balance(data, save_data)
        elif choice == "8":
            print("👋 Logging out...\n")
            break
        else:
            print(" Invalid option!\n")



# MAIN MENU (ENTRY POINT)

def main_menu():
    while True:
        print(" WELCOME TO DEVELOPERS BANK ")
        print("1. Manager Login")
        print("2. Staff Login")
        print("3. Customer Login")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager_login(data, save_data)
        elif choice == "2":
            staff_login(data, save_data)
        elif choice == "3":
            customer_login(data, save_data)
        elif choice == "4":
            print("Goodbye! Have a nice day.\n")
            break
        else:
            print("Invalid choice. Try again.\n")



main_menu() 
