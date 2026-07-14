#!/usr/bin/env python3

""" 
list_manager.py  - Lists (Lab 356.2)
Manage a list of integers with add, remove, and display operations.
Written by: Jean M Lauture
Date: July 14, 2026
"""

# ==========================================
# Task 2: List Management with Error Handling
# ==========================================
numbers = []

while True:
    print("\nList Manager")
    print("a. Add a number")
    print("b. Remove a number")
    print("c. Display the list")
    print("d. Quit")

    choice = input("Enter your choice: ").lower()

    if choice == "a":
        try:
            number = int(input("Enter an integer: "))
            numbers.append(number)
            print("Number added.")
        except ValueError:
            print("Error: Please enter a valid integer.")

    elif choice == "b":
        try:
            index = int(input("Enter the index to remove: "))
            removed = numbers.pop(index)
            print(f"Removed {removed}")
        except ValueError:
            print("Error: Index must be an integer.")
        except IndexError:
            print("Error: Invalid index.")

    elif choice == "c":
        print("Current List:", numbers)

    elif choice == "d":
        print("Goodbye!")
        break

    else:
        print("Error: Invalid menu choice.")
