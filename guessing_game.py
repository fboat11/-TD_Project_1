"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

print(" Welcome to the Number Guessing Game!!!  ")
print("Guess a number between 1 and 20. Good luck!!!")

solution = random.randrange(1, 20)

def start_game():
    attempts = 1
    while True:
        try:
            number_guessed = int(input("Please guess a number: "))
            
            while  number_guessed != solution:
                
                attempts += 1
                if number_guessed > solution:
                    print("It's lower")
                    number_guessed = int(input("Please guess another number: "))
                else:
                    print("It's higher ")
                    number_guessed = int(input("Please guess another number: "))
        except ValueError:
            print ("Sorry, entry is not a valid number ")
            continue
            
        else:
            print("Got it. You had", attempts,"attempts")
            print("Thanks for playing")
            break

start_game()   

    
  


