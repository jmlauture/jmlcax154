#Working with Bitwise Operators in Python
#Bitwise operators are used to perform bit-level operations on integers. 
#They operate on the binary representation of the numbers. 
#Here are some common bitwise operators in Python:
#1. Bitwise AND (&): This operator performs a logical AND operation on each bit of the numbers.
READ = 4  # In binary: 0100
WRITE = 2  # In binary: 0010
EXECUTE = 1  # In binary: 0001

# Using bitwise AND to check permissions
# Hint: focus on the write bit value (2) to check if the write permission is set.
# rw =110, r = 100, w = 010, x = 001, wx=011, rwx=111
result_and = READ & WRITE  # Result: 0 (In binary: 0000)
#2. Bitwise OR (|): This operator performs a logical OR operation on each bit of the numbers.
result_or = READ | WRITE  # Result: 6 (In binary: 0110)
#3. Bitwise XOR (^): This operator performs a logical XOR operation on each bit of the numbers.
result_xor = a ^ b  # Result: 6 (In binary: 0110)
#4. Bitwise NOT (~): This operator performs a logical NOT operation on each bit of the number.
