"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jiri Skalicky
email: Skalicky.jiri92@gmail.com
discord: skala7142
"""

import random

def greet():
    print("Hi there!")
    print("-" * 50)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 50)

    
def generate_number():
    generated_number = "".join(random.sample("123456789", 4))   
    return generated_number

def control_guess(guess):
    errors = []               

    if len(guess) != 4:                
        errors.append("4 numbers are needed")
    elif not guess.isdigit():
        errors.append("Only numbers between 0-9 are allowed")
    elif len(set(guess)) != len(guess):
        errors.append("Each number must be unique")
    elif guess[0] == '0':
        errors.append("4 digit number can't start with 0")

    return errors if errors else True          

def bulls_and_cows(guess, generated):
    bulls = 0
    cows = 0
    for num in range(4):
        if guess[num] == generated[num]:
            bulls += 1
        elif guess[num] in generated:
            cows += 1
    return bulls, cows

def attempts(guess_count):
    if guess_count < 4:
        print("You are a genius or lucky!")
    elif guess_count >= 4 and guess_count <= 12:
        print("You did well!")
    else:
        print("That was good, but you can do even better next time !")


def game():
    greet()
    generated = generate_number()  
    guessed_correctly = False  
    guess_count = 0
    while not guessed_correctly:
        guess = input("Guess 4 digit number: ")
        
        result = control_guess(guess)
        if result != True:
            for error in result:
                print("-", error)
            continue 
        guess_count += 1
        
        if guess == generated:
            print(f"Congratulations! You guessed the correct number: {generated}")
            guessed_correctly = True  
        else:
            bulls, cows = bulls_and_cows(guess, generated)
            print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

    attempts(guess_count)
    

game()













