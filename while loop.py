# Print the sequence 10 9 8 7 6 5

i = 10

while i >= 5:
    print(i)
    i = i - 1


# Print the sequence 9 6 3 0

i = 9

while i >= 0:
    print(i)
    i = i - 3


# Display odd digits from a given number

n = 1234

while n != 0:
    ld = n % 10

    if ld % 2 != 0:
        print(ld)

    n = n // 10


# Print statements using end

print("Hello", end=" ")
print("Good Evening !")
