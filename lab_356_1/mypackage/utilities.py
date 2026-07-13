#!/usr/bin/env python3

""" 
utilities.py  - Custom Modules (Lab 356.1)
An implementation of using custom modules.
Written by: Jean M Lauture
Date: July 12, 2026
"""
# ==========================================
# Task 2: Creating Custom Modules
# ==========================================

def greet(name):
    return f"Hello, {name}!"

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    