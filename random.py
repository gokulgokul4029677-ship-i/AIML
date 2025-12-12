import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 10)  # Random number between 1 and 100
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"🎉 Correct! The number was {number}.")
                print(f"You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")

number_guessing_game()
