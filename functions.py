# --------------------- Normal Functions ---------------------

# Function without input and without return

def sayHello():
    print("Hello ! Good Afternoon")

sayHello()


# -------------------------------------------------------------

# Function with input and without return

def displayName(fname):
    print("My name is", fname)

displayName("Janu")


# -------------------------------------------------------------

# Function without input and with return

def displayMsg():
    return "Hello Good afternoon"

print(displayMsg())


# -------------------------------------------------------------

# Function with input and with return

def displayName(fname):
    return "My name is " + fname

print(displayName("Janu"))


def addTwo(a, b):
    return f"Sum = {a + b}"

print(addTwo(10, 20))


# -------------------------------------------------------------

def sayHello():
    print("Hello")

sayHello()


# ---------------- Conditional Statements -------------------

def checkEven():
    if 10 % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(checkEven())


def checkEvenNumber(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(checkEvenNumber(10))