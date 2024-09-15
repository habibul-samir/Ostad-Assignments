import random

def theNumber():
    cookie = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game! \nTry to guess the number between 1 and 100.")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please enter a number from 1 to 100!")
            elif user_guess > cookie:
                print("Too high!") 
            elif user_guess < cookie:
                print("Too low!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Enter a number from 1 to 100!")

theNumber()

# MD. Habibul Basher
# Ostad : Assignment | Module 5 | 15th September