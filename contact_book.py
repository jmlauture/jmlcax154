"""
contact_book.py

Project: Simple Contact Book Console Application

Brief Write-Up:
This program uses a dictionary called contacts to store contact records.
The contact name is used as the key, and the phone number is used as the value.
Using a dictionary helps prevent duplicate names and makes it easy to search,
view, and delete contacts.

Program Structure:
- is_valid_phone(phone): checks if the phone number is reasonable.
- add_contact(contacts): adds a new contact if the name does not already exist.
- view_contacts(contacts): displays all contacts in alphabetical order.
- search_contact(contacts): searches by full or partial name.
- delete_contact(contacts): deletes a contact by name.
- show_menu(): displays the menu.
- main(): controls the program loop.

Challenges Solved:
- Duplicate names are prevented by checking if the name already exists.
- Invalid menu input is handled with try/except.
- Invalid phone numbers are rejected before saving.
- Empty contact lists are handled with friendly messages.
"""


def is_valid_phone(phone):
    """
    Checks whether the phone number is reasonable.

    For this simple project, a valid phone number:
    - Can contain digits, spaces, dashes, parentheses, or plus signs
    - Must have between 7 and 15 digits total
    """

    allowed_characters = "0123456789-+() "

    for char in phone:
        if char not in allowed_characters:
            return False

    digits_only = ""

    for char in phone:
        if char.isdigit():
            digits_only += char

    return 7 <= len(digits_only) <= 15


def add_contact(contacts):
    """
    Adds a new contact to the dictionary.
    The name can only exist once.
    """

    try:
        name = input("Enter contact name: ").strip()

        if name == "":
            print("Error: Name cannot be empty.")
            return

        if name in contacts:
            print("Error: This contact already exists.")
            return

        phone = input("Enter phone number: ").strip()

        if not is_valid_phone(phone):
            print("Error: Invalid phone number.")
            print("Use 7-15 digits. You may include spaces, dashes, parentheses, or +.")
            return

        contacts[name] = phone
        print(f"Contact '{name}' added successfully.")

    except Exception as e:
        print(f"An unexpected error occurred while adding the contact: {e}")


def view_contacts(contacts):
    """
    Displays all contacts.
    Contacts are sorted alphabetically by name.
    """

    try:
        if not contacts:
            print("The contact list is empty.")
            return

        print("\nAll Contacts:")
        print("-" * 30)

        for name in sorted(contacts):
            print(f"{name}: {contacts[name]}")

    except Exception as e:
        print(f"An unexpected error occurred while viewing contacts: {e}")


def search_contact(contacts):
    """
    Searches for a contact by full or partial name.
    """

    try:
        if not contacts:
            print("The contact list is empty.")
            return

        search_name = input("Enter name or part of name to search: ").strip().lower()

        if search_name == "":
            print("Error: Search text cannot be empty.")
            return

        matches_found = False

        print("\nSearch Results:")
        print("-" * 30)

        for name, phone in contacts.items():
            if search_name in name.lower():
                print(f"{name}: {phone}")
                matches_found = True

        if not matches_found:
            print("No matching contact found.")

    except Exception as e:
        print(f"An unexpected error occurred while searching contacts: {e}")


def delete_contact(contacts):
    """
    Deletes a contact by exact name.
    """

    try:
        if not contacts:
            print("The contact list is empty.")
            return

        name = input("Enter the exact name of the contact to delete: ").strip()

        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print("Contact not found.")

    except Exception as e:
        print(f"An unexpected error occurred while deleting the contact: {e}")


def show_menu():
    """
    Displays the contact book menu.
    """

    print("\nContact Book Menu:")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def main():
    """
    Main program loop.
    Keeps showing the menu until the user chooses Exit.
    """

    contacts = {}

    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                add_contact(contacts)
            elif choice == 2:
                view_contacts(contacts)
            elif choice == 3:
                search_contact(contacts)
            elif choice == 4:
                delete_contact(contacts)
            elif choice == 5:
                print("Thank you for using the Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
