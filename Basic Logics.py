# Q1. Calculate profit percentage using selling price and cost price

cp = int(input("Enter the cost price: "))
sp = int(input("Enter the selling price: "))

profit = sp - cp
print("The profit is", profit)

profit_percentage = (profit / cp) * 100
print("The profit percentage is", profit_percentage, "%")


# Q2. Find the missing angle in a triangle by taking 2 angles

angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))

sum_of_angles = angle1 + angle2
missing_angle = 180 - sum_of_angles

print("The missing angle is", missing_angle, "degrees")


# Q3. Find the last digit of a given number

number = int(input("Enter the number: "))

last_digit = number % 10

print("The last digit is", last_digit)


# Q4. Calculate the average of three numbers

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

sum_of_numbers = n1 + n2 + n3
average = sum_of_numbers / 3

print("The average is", average)


# Q5. Remove the last digit of the given number
# Example: 352 -> 35

number = int(input("Enter the number: "))

result = number // 10

print("After removing the last digit:", result)


# Q6. Find the first digit of a four-digit number

number = int(input("Enter a four digit number: "))

first_digit = number // 1000

print("The first digit is", first_digit)


# Q7. Calculate the sum of first n natural numbers

n = int(input("Enter the number: "))

sum_of_n_numbers = n * (n + 1) // 2

print("The sum is", sum_of_n_numbers)


# Q8. Calculate the average of first 10 natural numbers

n = 10

sum_of_numbers = n * (n + 1) // 2
average = sum_of_numbers / n

print("The average of first 10 natural numbers is", average)


# Q9. Calculate the gross salary
# Basic salary, bonus percentage and incentives percentage

basic_salary = int(input("Enter the basic salary: "))
bonus_percentage = int(input("Enter the bonus percentage: "))
incentives_percentage = int(input("Enter the incentives percentage: "))

bonus = (bonus_percentage / 100) * basic_salary
incentives = (incentives_percentage / 100) * basic_salary

gross_salary = basic_salary + bonus + incentives

print("The bonus is", bonus)
print("The incentives are", incentives)
print("The gross salary is", gross_salary)


# Q10. Calculate in-hand salary
# Basic salary, bonus, incentives, PF and health insurance

basic_salary = int(input("Enter the basic salary: "))
bonus_percentage = int(input("Enter the bonus percentage: "))
incentives_percentage = int(input("Enter the incentives percentage: "))
pf_percentage = int(input("Enter the PF percentage: "))
health_insurance_percentage = int(input("Enter the health insurance percentage: "))

bonus = (bonus_percentage / 100) * basic_salary
incentives = (incentives_percentage / 100) * basic_salary

pf = (pf_percentage / 100) * basic_salary
health_insurance = (health_insurance_percentage / 100) * basic_salary

gross_salary = basic_salary + bonus + incentives

inhand_salary = gross_salary - pf - health_insurance

print("The gross salary is", gross_salary)
print("The in-hand salary is", inhand_salary)


# Q11. Swap two numbers using a third variable

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)


# Q12. Swap two numbers without using a third variable

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
