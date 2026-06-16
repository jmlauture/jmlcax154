# Checking grades from 0 to 100
# We assume the user enters a valid number for this task
#
#Terminal command: python3 grade_checker.py

user_input = int(input("Enter a grade from 0..100 "))

if user_input >= 90 and user_input < 100:
    grade = "A"
    print("Your grade is: ", grade)

elif user_input >= 80 and user_input < 90:
    grade = "B"
    print("Your grade is: ", grade)

elif user_input >= 70 and user_input < 80:
    grade = "C"
    print("Your grade is: ", grade)

elif user_input >= 60 and user_input < 70:
    grade = "D"
    print("Your grade is: ", grade)

else:
    grade = "F"
    print("Your grade is: ", grade)


if grade in ["A", "B", "C"]:
    print("Congradulations! You've passed")
else:
       print("Continue to practice! You're not far off. You will pass next time.")


# Output Example:
# Enter a grade from 0..100 90
# Your grade is:  A
# Congradulations! You've passed

# Enter a grade from 0..100 81
# Your grade is:  B
# Congradulations! You've passed

# Enter a grade from 0..100 77
# Your grade is:  C
# Congradulations! You've passed

# Enter a grade from 0..100 58
# Your grade is:  F
# Continue to practice! You're not far off. You will pass next time.
