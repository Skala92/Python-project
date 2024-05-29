"""
projekt_1.py: first project in Engeto Online Python Akademie
author: Jiri Skalicky
email:  Skalicky.jiri92@gmail.com
discord: skala7142
"""

TEXTS = [
    '''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.
    ''',
    '''
    At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.
    ''',
    '''
    The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.
    '''
]

def login():
    users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "123"}
    valid_user = input("username: ")
    password = input("password: ")
    return valid_user, password, users

def select_text():
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    selected_text = input(f"Enter a number between 1 and {len(TEXTS)} to select: ")
    return selected_text

def analyze_text(text):
    words = text.split()
    count_words = len(words)
    tcase_words, upcase_words, lcase_words, non_num_char, sum_num_ch = 0, 0, 0, 0, 0
    word_length = {}

    for word in words:
        stripped_word = word.strip(",.!?")
        if stripped_word.istitle():
            tcase_words += 1
        if stripped_word.isupper() and not stripped_word[0].isnumeric():
            upcase_words += 1
        if stripped_word.islower():
            lcase_words += 1
        if stripped_word.isnumeric():
            non_num_char += 1
            sum_num_ch += int(stripped_word)
        length = len(stripped_word)
        if length > 0:
            if length in word_length:
                word_length[length] += 1
            else:
                word_length[length] = 1

    print("There are", count_words, "words in the selected text.")
    print("There are", tcase_words, "titlecase words.")
    print("There are", upcase_words, "uppercase words.")
    print("There are", lcase_words, "lowercase words.")
    print("There are", non_num_char, "numeric strings.")
    print("The sum of all the numbers is", sum_num_ch)

    print("-" * 40)
    print(f"LEN | {'OCCURRENCES':^25} | NR.")
    print("-" * 40)

    for length in sorted(word_length.keys()):
        occurrences = word_length[length]
        graph = "*" * occurrences
        print(f"{length:3} | {graph.ljust(25)} | {occurrences}")

def main():
    valid_user, password, users = login()
    if valid_user in users and users[valid_user] == password:
        print("-" * 40)
        print("Welcome to the app,", valid_user)
        selected_text = select_text()
        if selected_text.isdigit():                          
            selected_text = int(selected_text)
            if 1 <= selected_text <= len(TEXTS):             
                text_to_analyze = TEXTS[selected_text - 1]
                analyze_text(text_to_analyze)
            else:
                print("Invalid selection. Terminating the program...")
        else:
            print("Invalid input. Please enter a number between 1 and", len(TEXTS), ".")
    else:
        print("Unregistered user, terminating the program...")

if __name__ == "__main__":
    main()