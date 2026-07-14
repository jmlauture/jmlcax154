#!/usr/bin/env python3

""" 
age_validator.py  - Age Validation (Lab 356.2)
Validate a user-input age and ensure it is within a reasonable range.
Written by: Jean M Lauture
Date: July 14, 2026
"""
# ==========================================
# Task 3: Age Validation
# ==========================================
def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")
    return True

try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Age accepted.")
except ValueError as e:
    print("Error:", e)
