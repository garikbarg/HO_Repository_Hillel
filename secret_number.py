import random
secret_number = random.randint(1, 50)
print("Game 'Guess number'!")
print("You need guess number from 1 to 50.")
while True:
    guess = int(input("Enter number:"))

    if guess < secret_number:
        print("number is bigger.")
    elif guess > secret_number:
        print("number is smaller.")
    else:
        print(f"Congratulations! YOU WIN {secret_number}.")
        break