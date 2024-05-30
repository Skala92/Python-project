"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jiri Skalicky
email: Skalicky.jiri92@gmail.com
discord: skala7142
"""

import random

def greet():
    """
    Prints a greeting message.
    """
    print("Hi there!")
    print("-" * 50)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 50)

def generate_number():
    """
    Generates a random 4-digit number with unique digits where the first digit is between 1 and 9.
    
    Returns:
        str: A string representing the generated 4-digit number.
    """
    digits = list("0123456789")
    first_digit = random.choice(digits[1:])  
    digits.remove(first_digit)
    other_digits = random.sample(digits, 3)  
    generated_number = first_digit + "".join(other_digits)
    return generated_number

def control_guess(guess):
    """
    Checks if the guessed number meets the game's requirements and generates error messages if not.
    
    Args:
        guess (str): The player's guessed number.
    
    Returns:
        list or bool: A list of error messages if the guess is invalid, or True if the guess is valid.
    """
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
    """
    Calculates the number of bulls and cows in a guess compared to the generated number.
    
    Args:
        guess (str): The player's guessed number.
        generated (str): The generated 4-digit number.
    
    Returns:
        tuple: A tuple containing the number of bulls and cows.
    """
    bulls = 0
    cows = 0
    for num in range(4):
        if guess[num] == generated[num]:
            bulls += 1
        elif guess[num] in generated:
            cows += 1
    return bulls, cows

def attempts(guess_count):
    """
    Prints a message based on the number of attempts taken to guess the number.
    
    Args:
        guess_count (int): The number of attempts made by the player.
    """
    if guess_count < 4:
        print("You are a genius or lucky!")
    elif 4 <= guess_count <= 12:
        print("You did well!")
    else:
        print("That was good, but you can do even better next time!")

def get_input(input_message):
    """
    Function to get input from the user or test scenarios.
    
    Args:
        input message (str): The input message to display to the user.
    
    Returns:
        str: The user's input.
    """
    return input(input_message)

def game():
    """
    Main function to run the Bulls and Cows game.
    """
    greet()
    generated = generate_number()
    guessed_correctly = False
    guess_count = 0
    while not guessed_correctly:
        guess = get_input("Guess 4 digit number: ")

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

if __name__ == "__main__":
    game()