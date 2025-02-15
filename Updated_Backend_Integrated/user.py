from database import add_user, get_all_users, update_crisis_mode

def register_user(user_id, name, email):
    """
    Registers a new user by adding them to the Google Sheets database.
    """
    add_user(user_id, name, email)
    print(f"User registered: {name} ({email})")

def list_users():
    """
    Retrieves and displays all registered users.
    """
    users = get_all_users()
    if users:
        print("\nRegistered Users:")
        for user in users:
            print(f"ID: {user['user_id']} | Name: {user['name']} | Email: {user['email']} | Crisis Mode: {user['crisis_mode_status']}")
    else:
        print("No users found.")

def toggle_crisis_mode(user_id, status):
    """
    Updates the user's crisis mode status (ON/OFF).
    """
    update_crisis_mode(user_id, status)
    status_text = "ON" if status else "OFF"
    print(f"Crisis Mode for {user_id} set to {status_text}")

# Example usage
if __name__ == "__main__":
    while True:
        print("\nUser Management Menu")
        print("1. Register User")
        print("2. List Users")
        print("3. Toggle Crisis Mode")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            user_id = input("Enter User ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            register_user(user_id, name, email)
        
        elif choice == "2":
            list_users()

        elif choice == "3":
            user_id = input("Enter User ID: ")
            status = input("Enable Crisis Mode? (yes/no): ").strip().lower() == "yes"
            toggle_crisis_mode(user_id, status)

        elif choice == "4":
            print("Exiting User Management.")
            break

        else:
            print("Invalid choice. Please select a valid option.")
