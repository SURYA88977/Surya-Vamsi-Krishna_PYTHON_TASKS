
# =======================================
# Single Inheritance — 3
# 1. BankAccount → SavingsAccount
#    - Method: calculate_interest()
# 2. Book → EBook
#    - Method: read()
# =========================================

class BankAccount:
    def calculate_interest(self):
        print("General bank interest")

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings account interest is 6%")

# Bank=BankAccount()
# Bank.calculate_interest()
# account = SavingsAccount()
# account.calculate_interest()


class Physical_Book:
    def Book(self):
        print("The orginal Book")
class E_Book(Physical_Book):
    def Book(self):
        print(" I am the Electronic version of the orginal one")

# ebook=E_Book()
# ebook.Book()


# =========================================
# Multilevel Inheritance — 3
#1. school -> intermediate_College_ -> Degree_Collage
#    - Method: study()
# 2.Restaurant → Dine_in -> Take_Away -> Online_order
#  method: Order
# =========================================


#1. school -> intermediate_College_ -> Degree_Collage
#    - Method: study()
class School:
    def Study(self):
        print ("I am Studying in School ")
class intermediate_College(School):
    def Study(self):
        print("I am Studying in intermediate_College")
class Degree_College(intermediate_College):
    def Study(self):
        print("I am studying in Degree college")

# degree=Degree_College()
# degree.Study()
# inter=intermediate_College()
# inter.Study()
# school=School()
# school.Study()

# 2.Restaurant → Dine_in -> Take_Away -> Online_order
#  method: Order_type

class Dine_in:
    def Order_type(self):
        print("I prefer to order at Restaurant")

class Take_Away(Dine_in):
    def Order_type(self):
        print("I prefer to Take_Away")

class Online_order(Take_Away):
    def Order_type(self):
        print("I prefer to Online_order")

# R1=Dine_in()
# R1.Order_type()

# R1=Take_Away()
# R1.Order_type()

# R1=Online_order()
# R1.Order_type()


# ===========================================
# Hierarchical Inheritance
# 1.Payment → Cash / Card
# Method: pay()

# 2. SocialMedia → Instagram / YouTube
# - Method: post()
# ===========================================


# 1.Payment → Cash / Card
# Method: pay()
class Payment:
    def pay(self):
        print("Making a payment")

class Cash(Payment):
    def pay(self):
        print("paying with Cash")

class UPI_PAYTM(Payment):
    def pay(self):
        print("PAYTM karo.....")

p1 = Cash()
p1.pay()
p2 = UPI_PAYTM()
p2.pay()

# 2. SocialMedia → Instagram / YouTube
# - Method: post()
class SocialMedia:
    def post(self):
        print("Posting video")

class instagram(SocialMedia):
    def post(self):
        print("Posting reel ")

class YouTube(SocialMedia):
    def post(self):
        print("uploding short")

n=instagram()
n.post()
y=YouTube()
y.post()

