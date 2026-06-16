# tuples_dicts.py
# Demonstrates tuples and dictionaries

# Create a tuple containing the months of the year
months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

# Print the first and last month
print("The first month of the year is:", months[0])
print("The last month of the year is:", months[-1])

# Demonstrate tuple immutability
try:
    months[0] = "NewMonth"
except TypeError as e:
    print(f"Tuples are immutable, error: {e}")

print("\n--- Student Dictionary ---")

# Create a dictionary of students and grades
students = {
    "Lisa": 90,
    "Bob": 85,
    "Charlie": 92,
    "Diana": 88
}

# Add a new student
students["James"] = 97

# Print all student names and grades
print("\nAll students and grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")

# Update an existing student's grade
students["Bob"] = 93

# Print the updated entry
print("\nUpdated grade:")
print(f"Bob: {students['Bob']}")

# Print all students and grades in formatted form
print("\nFormatted student list:")
for name, grade in students.items():
    print(f"{name}: {grade}")