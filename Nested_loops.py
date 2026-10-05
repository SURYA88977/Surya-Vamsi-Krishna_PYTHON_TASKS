# 1. Sum of Prime Numbers
# Find the sum of all prime numbers between 20 and 150.

total = 0

for j in range(20, 151):
    n = j
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count == 2:
        total = total + n

print("Sum of prime numbers =", total)


# 2. Average of Perfect Numbers
# Find the average of all perfect numbers between 1 and 1000.

total = 0
count = 0

for j in range(1, 1001):
    n = j
    factor_sum = 0

    for i in range(1, n):
        if n % i == 0:
            factor_sum = factor_sum + i

    if factor_sum == n:
        print(n)
        total = total + n
        count = count + 1

average = total / count

print("Average =", average)


# 3. Leap Years in a Range
# Print all leap years between 1900 and 2026.

for i in range(1900, 2027):
    if (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
        print(i)


# 4. Palindrome Numbers
# Print all palindrome numbers between 100 and 500.

for i in range(100, 501):
    n = i
    original_number = n
    reverse = 0

    while n != 0:
        last_digit = n % 10
        reverse = reverse * 10 + last_digit
        n = n // 10

    if original_number == reverse:
        print(original_number)


# 5. Digit Sum = 10
# Print all numbers between 120 and 850
# whose digit sum is exactly 10.

for i in range(120, 851):
    n = i
    original_number = n
    digit_sum = 0

    while n != 0:
        last_digit = n % 10
        digit_sum = digit_sum + last_digit
        n = n // 10

    if digit_sum == 10:
        print(original_number)


# 6. Pairs with Target Sum
# Print all pairs (a, b) between 1 and 50
# whose sum is 30.
# Print each pair only once.

for j in range(1, 51):
    for i in range(j, 51):
        if i + j == 30:
            print(j, i)


# 7. Exactly 3 Factors
# Print all numbers between 10 and 300
# that have exactly 3 factors.

for j in range(10, 301):
    n = j
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count == 3:
        print(n)


# 8. Prime Factors
# Print the prime factors of every number between 20 and 50.

for j in range(20, 51):
    n = j

    print("Prime factors of", n, ":", end=" ")

    for i in range(1, n + 1):

        # Check whether i is a factor of n
        if n % i == 0:

            # Check whether i is prime
            count = 0

            for k in range(1, i + 1):
                if i % k == 0:
                    count = count + 1

            if count == 2:
                print(i, end=" ")

    print()


# 9. Armstrong Numbers
# Print all Armstrong numbers between 100 and 999.

for j in range(100, 1000):

    n = j
    original_number = n
    digit_count = 0

    # Count the number of digits
    while n != 0:
        digit_count = digit_count + 1
        n = n // 10

    n = original_number
    total = 0

    # Calculate Armstrong value
    while n != 0:
        last_digit = n % 10
        result = last_digit ** digit_count
        total = total + result
        n = n // 10

    if total == original_number:
        print(original_number)


# 10. Maximum Factors
# Find the number between 50 and 150
# that has the maximum number of factors.

max_count = 0
max_number = 0

for j in range(50, 151):

    n = j
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count > max_count:
        max_count = count
        max_number = n

print("Number =", max_number)
print("Factors =", max_count)
