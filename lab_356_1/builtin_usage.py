#!/usr/bin/env python3

""" 
builtin_usage.py  - Built-in Modules (Lab 356.1)
An implementation of using built-in modules like math, random, and platform.
Written by: Jean M Lauture
Date: July 12, 2026
"""
# ==========================================
# Task 1: Using Built-in Modules
# ==========================================
import math
import random   
import platform

for i in range(100):
    r = random.randint(1, 100)
    print("The random number is:", r)

    print("The square root of", r, "is:", math.sqrt(r))
    print("The floor of the square root of", r, "is:", math.floor(math.sqrt(r)))
    print("The integer part of the square root of", r, "is:", int(math.sqrt(r)))
    print()

       
# Platform information
print("The platform OS is:", platform.system())
print("The platform release is: Release", platform.release())
print("The Python version is:", platform.python_version())

# ==========================================
# Task 2: Creating and Importing a Custom Module
# ==========================================
