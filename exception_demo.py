# exception_demo.py
# Demonstrates raising and catching exceptions

def safe_divide(a, b):
    """
    Divides a by b.
    Raises a ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Demonstrate safe_divide with try/except/finally structure to call the function
try:
    num1 = 10
    num2 = 0  # Test value that will cause an exception

    result = safe_divide(num1, num2)
    print(f"The result is: {result}")

except ValueError as e:
    print(f"Error: {e}")

finally:
    print("Division operation completed")


print("\n--- Generic Exception Demo ---")

# Demonstrate catching a generic exception
try:
    value = int("xyz")  # Invalid conversion
    print(value)

except Exception as e:
    print(f"A generic exception occurred: {e}")