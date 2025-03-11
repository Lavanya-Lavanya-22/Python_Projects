

import random
import Guess

EASY_LEVELS_ATTEMPTS=10
HARD_LEVELS_ATTEMPTS=5


def set_level(level):
    if level=="easy":
        return EASY_LEVELS_ATTEMPTS
    else:
        return HARD_LEVELS_ATTEMPTS
        
def check_guess(guess,num,attempts):
    if num==guess:
        print(f"Correct guess the answer is  {num}")
    elif guess<num:
            print("Too Low")
            return attempts-1
    elif guess>num:
            print("Too high")
            return attempts-1

    print("Your guess is over ")
    
def game():
    print(Guess.logo)

    print("Think between 1 to 50 ")
    num=random.randint(1,50)

    level=input("Choose level of difficulty.. type 'easy' or 'hard' : ").lower()

    attempts=set_level(level)
    guess=0
    while guess !=num:
        
        guess=int(input(f"enter the guess , {attempts} You have : "))

        attempts=check_guess(guess,num,attempts)
        if attempts==0:
            print("Your guess is over ")
            return
        elif num!=guess:
            print("guess again")
game()
