"""Day3: Python Operators"""

# Arithmetic Operators
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor Division

# Assignment Operators
a = 10
b = 5
a += b  # Equivalent to a = a + b
print(a)
a -= b  # Equivalent to a = a - b
print(a)
a *= b  # Equivalent to a = a * b
print(a)
a /= b  # Equivalent to a = a / b
print(a)
a %= b  # Equivalent to a = a % b
print(a)
a **= b # Equivalent to a = a ** b
print(a)
a //= b # Equivalent to a = a // b
print(a)


# Comparison Operators
x = 5
y = 10
print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to


# Logical Operators

a = True
b = False

print(a and b)  # Logical AND
print(a or b)   # Logical OR
print(not a)    # Logical NOT


# Identity Operators

x = 5
y = 10

print(x is y)      # Identity operator "is"
print(x is not y)  # Identity operator "is not"


# Membership Operators

numbers = [1, 2, 3, 4, 5]

print(3 in numbers)     # Membership operator "in"
print(6 not in numbers) # Membership operator "not in"


# Bitwise Operators

x = 5  # 0101 in binary
y = 3  # 0011 in binary

print(x & y)  # Bitwise AND
print(x | y)  # Bitwise OR
print(x ^ y)  # Bitwise XOR
print(~x)     # Bitwise NOT
print(x << 1) # Bitwise left shift
print(x >> 1) # Bitwise right shift


# Python Operator Precedence

x = 5
y = 10
z = 15

result = x + y * z  # Operator precedence: Multiplication before addition

print(result)


