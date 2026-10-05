# =========  Single Inheritance  =============


# Without constructor

class Employee:
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def manage(self):
        print("Manager is managing the team")

m = Manager()
m.work()      
m.manage()


# Single Inheritance with Constructor

class Mobile:
    def __init__(self, Brand, Model, Price):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price

    def displayMobile_details(self):
        print("Mobile Brand : ", self.Brand)
        print("Mobile Model : ", self.Model)
        print("Mobile Price : ", self.Price)


class Smartphone(Mobile):
    def __init__(self, Brand, Model, Price, RAM, Storage):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price
        self.RAM = RAM
        self.Storage = Storage

    def display(self):
        print("Mobile Brand : ", self.Brand)
        print("Mobile Model : ", self.Model)
        print("Mobile Price : ", self.Price)
        print("RAM : ", self.RAM)
        print("Storage : ", self.Storage)


mob = Smartphone("I phone", "Duo", "300000", "8GB", "256GB")
mob.display()



# Single Inheritance with Constructor + Super()
class Movie:
    def __init__(self, movie_name, hero, heroine, director):
        self.movie_name = movie_name
        self.hero = hero
        self.heroine = heroine
        self.director = director

class Paradise(Movie):
    def __init__(self, movie_name, hero, heroine, director, language, rating):
        super().__init__(movie_name, hero, heroine, director)
        self.language = language
        self.rating = rating

    def display(self):
        print("Movie Name :", self.movie_name)
        print("Hero       :", self.hero)
        print("Heroine    :", self.heroine)
        print("Director   :", self.director)
        print("Language   :", self.language)
        print("Rating     :", self.rating)

p=Paradise("Paradise","Nani","Kayadu Lohar","Srikanth Odela","Telugu","3.5")

p.display()


# # 4.Single Inheritance with constructor + super() using a different real-world example

# class BankAccount:
#     def __init__(self, account_no, balance):
#         self.account_no = account_no
#         self.balance = balance
#         print("Bank Account Created")

# class SavingsAccount(BankAccount):
#     def __init__(self, account_no, balance, interest_rate):
#         super().__init__(account_no, balance)
#         self.interest_rate = interest_rate
#         print("Savings Account Created")

#     def display(self):
#         print("Account Number :", self.account_no)
#         print("Balance        :", self.balance)
#         print("Interest Rate  :", self.interest_rate, "%")

# s = SavingsAccount("SB12345", 50000, 6.5)
# s.display()







# #============ Multi Level Inheritance ========================

# # Without Constructor 

# class Restaurent:
#     def details(self):
#         self.restaurant_name="Paradise"
#         self.location="Hyderabad"
#     def res_details(self):
#         print("Restaurent Name : ", self.restaurant_name)  
#         print("Restaurent Location : ", self.location) 
# class Delivary(Restaurent):
#     def deli(self) :
#         self.delivary_partner="Swiggy"
#         self.delivary_time="30 min"
#     def del_details(self):
#         print("Restaurent Name : ", self.delivary_partner)  
#         print("Restaurent Location : ", self.delivary_time)
# class Customer(Delivary):
#     def cust(self) :
#         self.Customer_name="Rahul"
#         self.order_Amount=450
#     def cus_details(self):
#         print("Restaurent Name : ", self.Customer_name)  
#         print("Restaurent Location : ", self.order_Amount)

# c=Customer() 
# c.details()
# c.deli()
# c.cust()


# c.res_details()
# c.del_details()
# c.cus_details()         




# # With Constructor

# class Hospital:

#     def __init__(self,hospital_name,location,hospital_type):
#         self.hospital_name=hospital_name
#         self.location=location
#         self.hospital_type=hospital_type

#     def hospital_details(self):
#         print("Hospital Name : ",self.hospital_name)    
#         print("Location : ",self.location)    
#         print("Hospital Type : ",self.hospital_type)

# class Doctor(Hospital):

#     def __init__(self,hospital_name,location,hospital_type,doctor_name,age,specialization):
#         self.hospital_name=hospital_name
#         self.location=location
#         self.hospital_type=hospital_type
#         self.doctor_name=doctor_name
#         self.age=age
#         self.specialization=specialization

#     def doctor_details(self):
#         print("Hospital Name : ",self.hospital_name)    
#         print("Location : ",self.location)    
#         print("Hospital Type : ",self.hospital_type)    
#         print("Doctor Name : ",self.doctor_name)    
#         print("Doctor Age : ",self.age)    
#         print("Specialization : ",self.specialization)   

# class Specialist(Doctor):

#     def __init__(self,hospital_name,location,hospital_type,doctor_name,age,specialization,experience):
#         self.hospital_name=hospital_name
#         self.location=location
#         self.hospital_type=hospital_type
#         self.doctor_name=doctor_name
#         self.age=age
#         self.specialization=specialization
#         self.experience=experience

#     def specialist_details(self):
#         print("Hospital Name : ",self.hospital_name)    
#         print("Location : ",self.location)    
#         print("Hospital Type : ",self.hospital_type)    
#         print("Doctor Name : ",self.doctor_name)    
#         print("Doctor Age : ",self.age)    
#         print("Specialization : ",self.specialization)
#         print("Experience : ",self.experience)

# s=Specialist("Apollo Hospitals","Hyderabad","Multi Speciality","Dr.Rahul Sharma",42,"Cardiology","10 years")
# s.specialist_details()


# # Multiple Inheritance with constructor + super()

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print("Name       :", self.name)
        print("Salary     :", self.salary)
        print("Department :", self.department)

m = Manager("Rahul", 50000, "IT")

m.display()





class Student:                         
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_details(self):
        print("Name :", self.name)
        print("Age  :", self.age)

class Sports(Student):                 
    def __init__(self, name, age, sport):
        super().__init__(name, age)
        self.sport = sport

    def sports_details(self):
        print("Sport :", self.sport)

class CollegeStudent(Sports):          
    def __init__(self, name, age, sport, college, branch):
        super().__init__(name, age, sport)
        self.college = college
        self.branch = branch

    def college_details(self):
        print("College :", self.college)
        print("Branch  :", self.branch)


student = CollegeStudent("surya",21,"Cricket","adithya","BCA")

student.student_details()
student.sports_details()
student.college_details()