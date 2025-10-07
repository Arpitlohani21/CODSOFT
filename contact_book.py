# Contact Book (Task 5)
# Author: [Your Name]
# Internship: CODSOFT

contacts = {}

def show_menu():
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print(f"Contact '{name}' added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- All Contacts ---")
        for name, info in contacts.items():
            print(f"\nName: {name}")
            for key, value in info.items():
                print(f"{key}: {value}")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"\nName: {name}")
        for key, value in contacts[name].items():
            print(f"{key}: {value}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter contact name to update: ").strip()
    if name in contacts:
        print("Leave blank to keep existing value.")
        phone = input(f"Enter new phone [{contacts[name]['Phone']}]: ") or contacts[name]['Phone']
        email = input(f"Enter new email [{contacts[name]['Email']}]: ") or contacts[name]['Email']
        address = input(f"Enter new address [{contacts[name]['Address']}]: ") or contacts[name]['Address']
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

# Main Loop
while True:
    show_menu()
    choice = input("Enter choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
