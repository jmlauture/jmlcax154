"""
bubble_sort_demo.py
A script demonstrating the bubble sort algorithm for the Python class CAX-154.
"""
from ast import List


the_list = [64, 25, 12, 22, 11]
print("Original list:", the_list)
print("\nStarting bubble sort...\n")

# Bubble Sort Algorithm
n = len(the_list)
for i in range(n):
    # Last i elements are already in place
    for j in range(0, n-i-1):
        # Swap if the element found is greater than the next element
        if the_list[j] > the_list[j+1]:
            the_list[j], the_list[j+1] = the_list[j+1], the_list[j] 
    print(f"List after iteration #{i+1}: {the_list}")

print("\nThe final list after bubble sort:", the_list)


# Output Example:

# Original list: [64, 25, 12, 22, 11]

# Starting bubble sort...

# List after iteration #1: [25, 12, 22, 11, 64]
# List after iteration #2: [12, 22, 11, 25, 64]
# List after iteration #3: [12, 11, 22, 25, 64]
# List after iteration #4: [11, 12, 22, 25, 64]
# List after iteration #5: [11, 12, 22, 25, 64]

# The final list after bubble sort: [11, 12, 22, 25, 64]
