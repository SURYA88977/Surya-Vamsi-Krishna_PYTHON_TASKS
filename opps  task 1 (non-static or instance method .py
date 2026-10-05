# 1. Create an instance method to display MOBILE details.
#  without input and without return

class Mobile:
    def details(self):
        print("Comapany :- Motorola ")
        print("Parent Companey :- LENOVO ")

Details=Mobile()
Details.details()

# # 2. To check whether a number is even or odd. 
# # with input and without return

class Check_Even:
    def number(self,n):
        if n%2==0:
            print(f"{n} - is even")
        else:
            print(f"{n} - odd")

check= Check_Even()
check.number(35)


# # 3. return your laptop specification  . (without input and with return)

class laptop:
    def spetcs_of_device(self):
        return "Name: lenovo LOQ,  Ram:16gb , ssd:512gb , CPU:RYZEN5 ,  GPU:3050A 4gb "

lap=laptop()
print(lap.spetcs_of_device())


# # 4. Take a number and returns it is prime or not  (with input and with return)

class Check:
    def Check_prime(self,n):
        fact=0
        for i in range(1,n+1,1):
            if n%i==0:
                fact=fact+1
        if fact==2:
            return (f"{n} :  is a prime number ")
        else :
            return (f"{n} : is a composite number ")

che=Check()
print(che.Check_prime(8))



# create a Bank class demonstrating all four types of instance methods
class Bank:
    # 1. Without input and Without return
    def welcome(self):
        print("Welcome to HDFC Bank")

    # 2. With input and Without return
    def check_balance(self, balance):
        if balance >= 1000:
            print("Sufficient Balance")
        else:
            print("Low Balance")

    # 3. Without input and With return
    def bank_name(self):
        return "HDFC Bank"

    # 4. With input and With return
    def calculate_interest(self, amount):
        return amount * 2 / 100



b1 = Bank()
b1.welcome()
b1.check_balance(5000)
name = b1.bank_name()
print("Bank Name:", name)
interest = b1.calculate_interest(10000)
print("Interest:", interest)