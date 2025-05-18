# Control flow and logical operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Teen tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a photo taken? Type 'y' for Yes and 'n' for No: ").lower()
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you need to grow taller before you can ride.")

# Modulo operator (separate logic block)
number_to_check = int(input("What is the number you want to check? "))

if number_to_check % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


code challenge
#pizza order practice
