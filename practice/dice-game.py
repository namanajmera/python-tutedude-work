import random

print("Welcome to the Arena ...!!!")

print("Please enter to roll a dice or q to quit.")

while True:
    roll = input("Roll ==>")
    if roll == "q":
        break
    elif roll == '':
        print(f"Your number is {random.randint(1, 6)}");
    else:
        print("Invalid input")

print("Thank you for playing!")