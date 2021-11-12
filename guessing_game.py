import random

print(" Welcome to the Number Guessing Game!!!  ")
print("Guess a number between 1 and 20. Good luck!!!")

scores = [20]

def start_game():
    solution = random.randrange(1, 21)

    attempts = 1
    high_score = 21 - min(scores)
    print("High Score is  ", high_score, ", Higher is better" )

    while True:
        try:
            number_guessed = int(input("Please guess a number: "))

            if (1 <= number_guessed < 21):
                print("")

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
            scores.append(attempts)
            print("Got it. You had", attempts,"attempts")
            print("Thanks for playing")
            break

start_game()   
replay_game = input ("Would you like to replay game: Yes / No    ")
while replay_game.upper() == "YES":
    start_game()
    replay_game = input ("Would you like to replay game: Yes / No    ")
else:
    print("Good Game. Have a great Day!!!")
    


        


    
  


