"""
logic_bits.py
A short script demonstrating Python's logical and bitwise operators.
"""

print("==================================================")
print("PART 1: LOGICAL OPERATORS (Boolean Logic)")
print("==================================================")

# Prompt the user for input and convert to boolean values
# (Any non-empty string is True, except "0" or "false" which we handle manually)
user_in1 = input("Enter first boolean value (1/0 or True/False): ").strip().lower()
user_in2 = input("Enter second boolean value (1/0 or True/False): ").strip().lower()

# Convert user strings into actual Python Booleans
bool1 = user_in1 not in ('0', 'false', '')
bool2 = user_in2 not in ('0', 'false', '')

print(f"\nEvaluating: A = {bool1}, B = {bool2}")
print(f"  A and B : {bool1 and bool2}")
print(f"  A or B  : {bool1 or bool2}")
print(f"  not A   : {not bool1}")
print(f"  not B   : {not bool2}")

print("\n==================================================")
print("PART 2: BITWISE OPERATORS (Binary Operations)")
print("==================================================")

# Using two small integers: 5 and 3
a = 5
b = 3

# Helper function to print values nicely formatted as 8-bit binary strings
def print_bits(label, value):
    # If a bitwise NOT produces a negative number, bin() prefixes it with '-'
    # For clarity, we'll look at the 8-bit two's complement mask representation
    binary_str = format(value & 0xFF, '08b')
    print(f"{label:<15} : {value:<4} (Binary: {binary_str})")

print_bits("Integer A", a)
print_bits("Integer B", b)
print("-" * 45)

# 1. Bitwise AND (&) - Sets each bit to 1 if both bits are 1
print_bits("A & B (AND)", a & b)

# 2. Bitwise OR (|) - Sets each bit to 1 if at least one bit is 1
print_bits("A | B (OR)", a | b)

# 3. Bitwise XOR (^) - Sets each bit to 1 if only one of the bits is 1
print_bits("A ^ B (XOR)", a ^ b)

# 4. Bitwise NOT (~) - Inverts all the bits (Note: 5 becomes -6 due to Two's Complement)
print_bits("~A (NOT)", ~a)

# 5. Bitwise Left Shift (<<) - Shifts bits left by pushing zeros in from the right
print_bits("A << 1 (Left)", a << 1)

# 6. Bitwise Right Shift (>>) - Shifts bits right by pushing copies of the leftmost bit in from the left
print_bits("A >> 1 (Right)", a >> 1)
print("==================================================")


# Output Example:
# ==================================================
# PART 1: LOGICAL OPERATORS (Boolean Logic)
# ==================================================
# Enter first boolean value (1/0 or True/False): 6
# Enter second boolean value (1/0 or True/False): 9

# Evaluating: A = True, B = True
#   A and B : True
#   A or B  : True
#   not A   : False
#   not B   : False

# ==================================================
# PART 2: BITWISE OPERATORS (Binary Operations)
# ==================================================
# Integer A       : 5    (Binary: 00000101)
# Integer B       : 3    (Binary: 00000011)
# ---------------------------------------------
# A & B (AND)     : 1    (Binary: 00000001)
# A | B (OR)      : 7    (Binary: 00000111)
# A ^ B (XOR)     : 6    (Binary: 00000110)
# ~A (NOT)        : -6   (Binary: 11111010)
# A << 1 (Left)   : 10   (Binary: 00001010)
# A >> 1 (Right)  : 2    (Binary: 00000010)
# ==================================================