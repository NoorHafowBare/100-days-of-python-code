# code challenge
#pizza order practice
print("welcome to python pizza delivers")
size = input("what size pizza do you want? s, m, or l: ")
pepperoni = input("do you want pepperoni on your pizza? y or n")
extra_cheese = input("do you want extra cheese? y or n")
age = int(input("what is your age"))

#todo: work out how much they need to pay based on their size choice
bill = 0
free_pizza = False
# Check for old people first
if 45 <= age <= 55:
    free_pizza = True
    print("Everything is going to be okay. Enjoy your pizza and have a free health check on us!")
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

else:
    print("you typed wrong number")

# todo: work out how much to add their bill based on their pepperoni choice
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

#todo: workout if their final ammount based on whether if they want extra cheese
if extra_cheese == "yes":
    bill += 1

print(f"your final is ${bill}.")


