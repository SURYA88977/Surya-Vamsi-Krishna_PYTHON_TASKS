# resturant Task


print("----- Menu -----")
print("1. Biryani")
print("2. Chicken 65")
print("3. Veg Pulao")
print("4. Butter Chicken")
print("5. Paneer Tikka")

menu = int(input("Enter your choice: "))

match menu:
    case 1:
        print("Item: Biryani")
        print("Price: ₹250")
        print("Description: Fragrant basmati rice cooked with rice and chicken")

    case 2:
        print("Item: Chicken 65")
        print("Price: ₹180")
        print("Description: Crispy and spicy deep-fried chicken pieces")

    case 3:
        print("Item: Veg Pulao")
        print("Price: ₹220")
        print("Description: Fragrant saffron threads are delicately infused into the long-grain basmati rice")

    case 4:
        print("Item: Butter Chicken")
        print("Price: ₹350")
        print("Description: Chicken tossed in a tangy, creamy, butterlicious tomato-flavoured sauce")

    case 5:
        print("Item: Paneer Tikka")
        print("Price: ₹200")
        print("Description: Grilled paneer cubes marinated with spices and yogurt")

    case _:
        print("Sorry, not available. Choose another item..!")
        
# =====================================================================================================================

# ATM Task

print("----- ATM MENU -----")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice: "))

balance = 10000

match choice:
    case 1:
        print("Your balance is:", balance)

    case 2:
        deposit = int(input("Enter deposit amount: "))
        balance = balance + deposit
        print("Your updated balance is:", balance)

    case 3:
        withdraw = int(input("Enter withdrawal amount: "))

        if withdraw <= balance:
            balance = balance - withdraw
            print("Your updated balance is:", balance)
        else:
            print("Insufficient balance!")

    case 4:
        print("Thank you! Visit again ")

    case _:
        print("Invalid Input! Choose a valid option...")