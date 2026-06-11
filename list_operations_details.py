"""
list_operations.py
A script demonstrating various list manipulation operations for the Python class CAX-154.
"""

# Initialize an empty list
the_list = []

# print("Please enter 5 integers to fill the list:")

# Loop 5 times to collect user input
"""
for i in range(5):
    while True:
        try:
            # Prompt the user for an integer input
            user_input = int(input(f"Enter the integer #{i+1} for the list: "))
            # Add the valid integer to the list
            the_list.append(user_input)
            break
            
        except ValueError:
            # Handle cases where the input is not an integer
            print("Invalid input. Please enter a valid integer.")
        continue
"""
# For testing purposes, we will use a predefined list instead of the user input list
the_list = [5, 2, 9, 1, 3]

print("-- Step 2 ---")    
print(f"Your original list is: {the_list}")

# Step 3: Use sorted() to print a sorted version without modifying the original
print("\n--- Step 3 ---")
temporary_sorted = sorted(the_list)
print("Sorted list (using sorted()):", temporary_sorted)
print("Original list remains unchanged:", the_list)
print()

# Step 4: Use .sort() to sort the list in place, then print it
print("\n--- Step 4 ---")
the_list.sort()
print("List after in-place sort (using .sort()):", the_list)
print()

# Step 5: Add a new element to the list using append(), then print it
print("\n--- Step 5 ---")
the_list.append(25)
print("List after adding (appending) the integer 25:", the_list)
print()

# Step 6: Remove an element from the list using remove(), then print it
print("\n--- Step 6 ---")   
the_list.remove(the_list[2])  # Removing the 3rd integer (index 2)
print(f"List after removing the 3rd integer {the_list[2]}:", the_list)   

# Step 7: Use the reverse() method to reverse the list, then print it
print("\n--- Step 7 ---")
the_list.reverse()
print("Reversed list:", the_list)
print()


# Key Python Concepts to Note:
# sorted(numbers) vs numbers.sort(): As demonstrated in Step 3 and Step 4, 
# sorted() is a built-in function that returns a brand-new list object, leaving your original list alone. 
# .sort() is a list method that rearranges the items directly inside the original memory allocation, returning None.

# remove(value): This looks for the first occurrence of the actual value provided or indexed value in the list and removes it.  
# If the value is not found, it raises a ValueError. 
# and extracts it from the sequence, automatically shifting subsequent items down to fill the gap.

# Output:
# -- Step 2 ---
# Your original list is: [5, 2, 9, 1, 3]

# --- Step 3 ---
# Sorted list (using sorted()): [1, 2, 3, 5, 9]
# Original list remains unchanged: [5, 2, 9, 1, 3]


# --- Step 4 ---
# List after in-place sort (using .sort()): [1, 2, 3, 5, 9]


# --- Step 5 ---
# List after adding (appending) the integer 25: [1, 2, 3, 5, 9, 25]


# --- Step 6 ---
# List after removing the 3rd integer 5: [1, 2, 5, 9, 25]

# --- Step 7 ---
# Reversed list: [25, 9, 5, 2, 1]