# Lab 351-2: Data Types, Variables, Operators, and Basic I/O 
# Author: Jean Lauture
# To see the outputs of this code, 
# run it in a Python environment (like VS Code, Jupyter Notebook, PyCharm, 
# or the command line) 
# python3 lab351-2_1_types_and_vars.py  
#

name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("What is your height (in meter)? "))
print(f"Hello, my name is {name}. I am {age} years old and {height} meters tall.")    
print()

# Calculations with addition
# Let's calculate how old I will be in 5 years 
print(f"In 5 years, I will be {age+5} years old")
print()
# Calculations with multiplication
# Let's calculate the area of a rectangle with width 5.5 feet and height 2 feet
r_width = 5.5
r_height = 2
print(f"The area of a {r_width} x {r_height} rectangle is " + str(r_width * r_height) + " square feet.")
print()
# Calculations with multiplication, percentage and substraction 
# Computer Lab is 3 times the rectangle mentioned above, 
# my PC room is about 70% of the lab size 
# and the kids play room is 7 square feet less than his lab
print("Using multiplication", "percentage", "substraction", "separators", sep="-")
print("----------------------------------------------------------------")
print("His computer lab is 3 times the rectangle mentioned above with an area of " + str((r_width * r_height) * 3) +" feet,"
      + " \n my PC room is about 70% his lab size, " + str((r_width * r_height) * 3 * 0.7) +" feet,"
      + "\n and the kids play room is 7 square feet less than the lab, " + str((r_width * r_height) * 3 - 7) + ".")