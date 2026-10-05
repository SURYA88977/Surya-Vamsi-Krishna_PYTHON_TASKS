# Arithmetic Operators

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))

sum = a + b
print("a + b =", sum)

sub = a - b
print("a - b =", sub)

mul = a * b
print("a * b =", mul)

div = a / b
print("a / b =", div)

fdiv = a // b
print("a // b =", fdiv)

mod = a % b
print("a % b =", mod)

ans = a ** b
print("a ** b =", ans)


# Relational Operators

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# Logical Operators

a = False
b = False

print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)


# Assignment Operators

a = 15
print("Before a:", a)

a += 5        # a = a + 5 -> 15 + 5 = 20
print("a += 5:", a)

a -= 4        # a = a - 4 -> 20 - 4 = 16
print("a -= 4:", a)

a *= 3        # a = a * 3 -> 16 * 3 = 48
print("a *= 3:", a)

a /= 5        # a = a / 5 -> 48 / 5 = 9.6
print("a /= 5:", a)

a //= 2       # a = a // 2 -> 9.6 // 2 = 4.0
print("a //= 2:", a)

a %= 6        # a = a % 6 -> 4.0 % 6 = 4.0
print("a %= 6:", a)

a **= 2       # a = a ** 2 -> 4.0 ** 2 = 16.0
print("a **= 2:", a)


# Bitwise Operators

# AND operator
a = 11
b = 13
print("a & b =", a & b)

# OR operator
print("a | b =", a | b)

# XOR operator
print("a ^ b =", a ^ b)

# NOT operator
a = 7
print("~a =", ~a)

# Left-shift operator
a = 7
print("a << 1 =", a << 1)

# Right-shift operator
a = 7
print("a >> 2 =", a >> 2)

# Another left-shift example
a = 11
print("11 << 1 =", 11 << 1)
