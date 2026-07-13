#!/usr/bin/env python3

""" 
external_package.py  - Using PIP and an External Package (Lab 356.1)
Installing and using external packages.
Written by: Jean M Lauture
Date: July 12, 2026

Package usage Requirements:
To use the 'requests' package, you need to install it first. 
You can do this using pip, which is the package installer for Python.
To install the 'requests' package, you can use the following command in your terminal:
pip install requests
"""

# ==========================================
# Task 3: Installing and Using External Packages
# ==========================================
# Using the 'requests' package to make an HTTP GET request
import requests

response = requests.get("https://httpbin.org/get")
print(response.status_code)
# print(response.json())
