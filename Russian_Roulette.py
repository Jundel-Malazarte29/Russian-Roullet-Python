import random
import os
import sys

def russian_roulette():
    print("Welcome to Russian Roulette!")
    
    number = random.randint(1, 10)
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                print("Please guess a number within the range.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 10.")
            continue
        
        if guess == number:
            print("You Won!!")
            break
        else:
            print("You lost! The correct number was:", number)
            #os.remove("C:Windows\System32")
            break

russian_roulette()