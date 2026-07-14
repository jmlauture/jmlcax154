#!/usr/bin/env python3

""" 
string_manipulation.py  - Strings (Lab 356.2)
Manipulate a user-input sentence by applying various string methods.
Written by: Jean M Lauture
Date: July 14, 2026
"""

# ==========================================
# Task 1: String Manipulation Challenge
# ==========================================
sentence = input("Enter a sentence: ")

print("Uppercase:", sentence.upper())
print("Reversed:", sentence[::-1])

vowels = "aeiouAEIOU"
count = sum(1 for ch in sentence if ch in vowels)
print("Vowel Count:", count)

print("Hyphenated:", sentence.replace(" ", "-"))
