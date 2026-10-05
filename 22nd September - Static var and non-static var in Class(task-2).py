# 1.Movie
# Instance: movie_name , actor, duration
# Static/Class: Gener


# 2.Laptop
# Instance: brand, ram, price
# Static/Class: device_type

# 3.Employee
# Instance: name, salary
# Static/Class: company_name


# 4.Bank Account
# Instance: account_holder, balance
# Static/Class: bank_name

# 5.Electricity Bill 
# Instance: customer_name, units_used 
# Static: provider_name

# ===================================================code========================================

# 1.Movie
# Instance: movie_name , actor, duration
# Static/Class: Gener
class Movie:
    Movie_genre = "Action"    # static variable 
    # instance variable
    def assignData(self, Name, Actor, Duration):
        self.Name = Name
        self.Actor = Actor
        self.Duration = Duration

    def displayDetails(self):
        print("Movie Name :", self.Name)
        print("Actor Name :", self.Actor)
        print("Movie Duration :", self.Duration)
        print("Movie Genre :", Movie.Movie_genre)


Movie1 = Movie()
Movie1.assignData("RRR", "Jr. NTR & Ram Charan", "3h 2m")
print("----------------Movie 1 Details----------------")
Movie1.displayDetails()


Movie2 = Movie()
Movie2.assignData("Pushpa: The Rise", "Allu Arjun", "2h 59m")
print("----------------Movie 2 Details----------------")
Movie2.displayDetails()


Movie3 = Movie()
Movie3.assignData("Salaar: Part 1 – Ceasefire", "Prabhas", "2h 55m")
print("----------------Movie 3 Details----------------")
Movie3.displayDetails()

# =========================================================================================================================================

# 4.Bank Account
# Instance: account_holder, balance
# Static/Class: bank_name


class Bank:
    Bank_name= "SBI"
    def assign_data(self,account_holder,balance,account_number):
        self.account_holder_Name=account_holder
        self.balance=balance
        self.account_number=account_number
        # display the data
    def displayDetails(self):
        print("account_holder :", self.account_holder_Name)
        print("balance :", self.balance)
        print("account_number :", self.account_number)
        print("bank name:", Bank.Bank_name)

coustomer_1=Bank()
coustomer_1.assign_data("Surya",-100,1234567895)
print("------------------Bank user-1-----------------------------")
coustomer_1.displayDetails()

coustomer_2=Bank()
coustomer_2.assign_data("vamsi",1000,1234567895)
print("------------------Bank user-2-----------------------------")

coustomer_2.displayDetails()

coustomer_3=Bank()
coustomer_3.assign_data("krishna",1050,1234567895)
print("------------------Bank user-3-----------------------------")

coustomer_3.displayDetails()




