import random

print("Welcome to the number guessing game. We have a number that need to be guessed. You have 10 chances.")
print("The secret number is between 1 and 50")
print("You have 10 attempts left")

correctNumber = random.randint(1, 50)
count = 10;
while True:
    value = int(input("Guess the secret number:- "))
    if value == correctNumber:
        print(f"You guessed the secret number {correctNumber}")
        break
    else:
        count-=1
        if count == 0:
            print("You Lost...!!!")
            break
        print(f"Sorry, the secret number wasn't correct. You have {count} attempts left")
        continue

print("Thank you for playing!")