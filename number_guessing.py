'''
Description: The program generates a random number between 1 and 100, and the player has to guess the number. 
The program provides hints (higher or lower) until the player guesses correctly.
'''

import random

def number_guessing_game():
    print("Welcome to the number guessing game!")
    print("Guess the number between 1 to 100")

    number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        guess = int(input("Guess the number: "))
        attempts +=1

        if guess < number:
            print("Too low, please try again")
        elif guess > number:
            print("Too high, please try again")
        else:
            guess = True
            print(f"Congrats you have guessed the number {number} in {attempts} attempts")

number_guessing_game()