# ------------------------
# if-else 
# --------------------------------
#     1.Check whether a given number is a 3-digit number or not.
#     2.Check whether a given number is divisible by both 3 and 5 or not.
#     3.Check whether a given triangle is a valid triangle or not.
#      hint :The sum of any two sides should be greater than the third side.
#     4.Check whether a given number is a multiple of 10 or not.
# ---------------------
# if-elif-else
# -----------------------
# 1.Check the type of triangle based on its sides.
#         Equilateral, Isosceles, or Scalene.
# 2.Calculate the electricity bill based on units consumed.
#     0–100: ₹2/unit, 101–200: ₹3/unit, 201–300: ₹5/unit, above 300: ₹7/unit.
# 3.Display the age category.
#     Below 13 → Child, 13–19 → Teenager, 20–59 → Adult, 60 and above → Senior Citizen.
# 4.Calculate the discount based on shopping amount.
#     Below ₹1,000 → No discount, ₹1,000–₹4,999 → 10%, ₹5,000–₹9,999 → 20%, ₹10,000 and above → 30%.
# 5.Display the season based on the month number.
#     3–5 → Spring, 6–8 → Summer, 9–11 → Autumn, 12/1/2 → Winter.
# 6.Check whether a given year is a Leap Year or not.
#     Condition 1: year % 400 == 0
#     Condition 2: year % 4 == 0 and year % 100 != 0
# ---------------------------
# Nested if – Tasks
# --------------------------
# 1.Check whether a person is eligible to donate blood.
#     Age should be between 18 and 60. If eligible by age, weight should be above 50 kg.
# 2.Display the grade based on average only if the student has passed in all 4 subjects.
# 3.Check whether a student is eligible for a scholarship.
#     Age should be above 18. If eligible by age, score should be above 86.


# ===========================================================================================================

# If-else
# ------------------------------------------------------------------------------------------------------------------------
#  1.Check whether a given number is a 3-digit number or not
n=int(input("enter a number :"))
if n>=100 and n<=999:
    print(n, "is a 3 digit number")
else:
    print("is not a 3 digit number")


# 2.Check whether a given number is divisible by both 3 and 5 or not
n=int(input("enter a number :"))
if n%3==0 and n%5==0:
    print(n, "is divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")


# 3.Check whether a given triangle is a valid triangle or not.
a=int(input("enter a distance :"))
b=int(input("enter b distance :"))
c=int(input("enter c distance :"))
if a+b>c or a+c>b or b+c>a:
    print("It is a valid triangle")
else:
    print("Invalid triangle")


# 4.Check whether a given number is a multiple of 10 or not.
n=int(input("enter a number :"))
if n%10==0:
    print(n, "is a multiple of 10")
else:  
    print("not a multiple of 10")

# -----------------------------------------------------------------------------------------------------
# if-elif-else
#---------------------------------------------------------------------------------------------------------
# 1. Check the type of triangle based on its sides.
a=int(input("enter a distance :"))
b=int(input("enter b distance :"))
c=int(input("enter c distance :"))
if a==b and b==c:
    print("Equilateral Triangle")
elif a==b or b==c or c==a:
    print("Isosceles Triangle")
else:
    print("Scalene triangle")


# Calculate the electricity bill based on units consumed.
    # 0–100: ₹2/unit, 101–200: ₹3/unit, 201–300: ₹5/unit, above 300: ₹7/unit.
n=int(input("enter the units consumed ="))
bill=0
if(n>=0 and n<=100):
    bill=n*2
    print("Total electricity bill is :", bill)
elif (n>=101 and n<=200):
    bill=n*3
    print("Total electricity bill is :", bill)
elif (n>=201 and n<=300):
    bill=n*5
    print("Total electricity bill is :", bill)
else:
    bill=n*7
    print("Total electricity bill is :", bill)


# Display the age category.
    # Below 13 → Child, 13–19 → Teenager, 20–59 → Adult, 60 and above → Senior Citizen.
n=int(input("enter the age ="))
if(n<13):
    print("Child")
elif(n>=13 and n<=19):
    print("Teenager")
elif(n>=20 and n<=59):
    print("Adult")
else:
    print("Senior Citizen")


# Calculate the discount based on shopping amount.
    # Below ₹1,000 → No discount, ₹1,000–₹4,999 → 10%, ₹5,000–₹9,999 → 20%, ₹10,000 and above → 30%
p=int(input("enter the price ="))
d_p=0
total=0
if(p<1000):
    d_p=p
    total=d_p
elif(p>=1000 and p<5000):
    d_p=(10/100)*p
    total=p-d_p
elif(p>=5000 and p<10000):
    d_p=(20/100)*p
    total=p-d_p
else:
    d_p=(30/100)*p
    total=p-d_p
print("Total amount with discount applied is =", total)


# Display the season based on the month number.
    # 3–5 → Spring, 6–8 → Summer, 9–11 → Autumn, 12/1/2 → Winter.
m=int(input("enter the month number :"))
if(m>=3 and m<=5):
    print("It is a Spring season")
elif(m>=6 and m<=8):
    print("It is a Summer season")
elif(m>=9 and m<=11):
    print("It is a Autumn season")
else:
    print("It is a Winter season")


# Check whether a given year is a Leap Year or not.
    # Condition 1: year % 400 == 0
    # Condition 2: year % 4 == 0 and year % 100 != 0
y=int(input("enter the year :"))
if(y%400==0):
    print("it is a leap year")
elif(y%4==0 and y%100!=0):
    print("It is a leap year")
else:
    print("not a leap year")
# =============================================================================
# Nested -if- Tasks
# ==============================================================================

# 1.Check whether a person is eligible to donate blood.
a=int(input("enter your age :"))
w=int(input("enter your weight :"))
if(a>=18 and a<=60):
    if(w>50):
        print("person is eligible to donate blood")
    else:
        print("not eligible to donate blood")
else:
    print("not eligible to donate blood")


# 2.Display the grade based on average only if the student has passed in all 4 subjects.
sub1=int(input("enter sub1 marks :"))
sub2=int(input("enter sub2 marks :"))
sub3=int(input("enter sub3 marks :"))
sub4=int(input("enter sub4 marks :"))
if sub1>=35 and sub2>=35 and sub3>=35 and sub4>=35:
    avg=(sub1+sub2+sub3+sub4)/4
    if avg>=80:
        print("grade A")
    elif avg>=60:
        print("grade B")
    elif avg>=45:
        print("grade C")
    else:
        print("grade D")
else:
    print("Failed") 


#3.Check whether a student is eligible for a scholarship.
    # Age should be above 18. If eligible by age, score should be above 86.
a=int(input("enter your age :"))
score=int(input("enter your score :"))
if(a>18):
    if(score>86):
        print("student is eligible for scholarship")
    else:
        print("not eligible")
else:
    print("student is not eligible for scholarship")