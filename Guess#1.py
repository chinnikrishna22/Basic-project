import random
import time

number = random.randint(1, 200)

def intro():
    print("May I ask you for your name?")
    name = input()  # Asks for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def pick():
    guesses_taken = 0
    while guesses_taken < 6:  # If the number of guesses is less than 6
        time.sleep(0.25)
        enter = input("Guess: ")  # Inserts the place to enter guess
        try:  # Check if a number was entered
            guess = int(enter)  # Stores the guess as an integer instead of a string    

            if 1 <= guess <= 200:  # If they are in range
                guesses_taken += 1  # Adds one guess each time the player is wrong
                if guesses_taken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    elif guess > number:
                        print("The guess of the number that you have entered is too high")
                    elif guess != number:
                        time.sleep(0.5)
                        print("Try Again!")
                if guess == number:
                    break  # If the guess is right, then we are going to jump out of the while block

            elif guess > 200 or guess < 1:  # If they aren't in the range
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 200")

        except ValueError:  # If a number wasn't entered
            print("I don't think that " + enter + " is a number. Sorry")

    if guess == number:
        guesses_taken = str(guesses_taken)
        print('Good job, ' + name + '! You guessed my number in ' + guesses_taken + ' guesses!')

    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))

play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    intro()
    pick()
    print("Do you want to play again? (yes/no)")
    play_again = input()

print("Thanks for playing!")
