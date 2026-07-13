#!/usr/bin/env python3

""" 
use_utilities.py  - Using Custom Modules (Lab 356.1)
An implementation of using custom modules.
Written by: Jean M Lauture
Date: July 12, 2026
"""
# ==========================================
# Task 2: Importing Custom Modules
# ==========================================

from mypackage import utilities

def main():
    # Using the greet function from the utilities module
    name = "James"
    greeting = utilities.greet(name)
    print(greeting)

    # Using the factorial function from the utilities module
    number = 5
    fact_result = utilities.factorial(number)
    print(f"The factorial of {number} is {fact_result}")

if __name__ == "__main__":
    main()

