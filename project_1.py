"""
projekt_1.py: first project in Engeto Online Python Akademie
author: Jiri Skalicky
email:  Skalicky.jiri92@gmail.com
discord: skala7142
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"123"}

spec_char1 = "-"
spec_char2 = "*"

valid_user = input("username:")
password = input("password:")


if valid_user in users and users[valid_user] == password:
    print(spec_char1 * 40)
    print("Welcome to the app,", valid_user)
    print("We have 3 texts to be analyzed.")
    print(spec_char1 * 40)   
    selected_text = input("Enter a number between 1 and 3 to select:")
    print(selected_text)
    
    if selected_text.isdigit():                      # Control if input is digit
        selected_text = int(selected_text) 
    if 1 <= selected_text <= 3:                      # Control if its between 1-3
        text_to_analyze = TEXTS[selected_text - 1]   # [0,1,2]
        words = text_to_analyze.split()              #split selected text 
        count_words = len(words)                     #counts number of words in selected text
        print("There are", count_words, "words in the selected text.") 
        
        tcase_words = []   
        for word in words:
            if word.istitle():                       # Finds words starting with capitals
                tcase_words.append(word)
        number_tc_words = len(tcase_words)
        print("There are", number_tc_words, "titlecase words.")

        upcase_words = []
        for word in words:
            if word.isupper():                       # Finds words starting with uppercase 
                upcase_words.append(word)
        number_up_words = len(upcase_words)
        print("There are", number_up_words, "uppercase words.")

        lcase_words = []
        for word in words:
            if word.islower():                       # Finds words starting lowercase
                lcase_words.append(word)
        number_lc_words = len(lcase_words)
        print("There are", number_lc_words, "lowercase words.")

        non_num_char = []
        for word in words:
            if word.isnumeric():                     # Finds non numeric characters in text
                non_num_char.append(word)
        non_num_char_count = len(non_num_char)
        print("There are", non_num_char_count, "numeric strings.")
        
        sum_num_ch = []
        for word in words:
            if word.isnumeric():                     # Finds non numeric characters and sum them
                sum_num_ch.append(int(word))
        total_sum = sum(sum_num_ch)
        print("The sum of all the numbers", total_sum)   

        word_length = {}
        for word in words:
            length = len(word.strip())                      # Find lengths of words, and strip them from empty spaces
            if length == 0:
                continue
            if length in word_length:
                word_length[length] += 1 
            else:
                word_length[length] = 1

        print(spec_char1 * 40)
        print(f"LEN | {'OCCURRENCES':^25} | NR.")
        print(spec_char1 * 40)

        for length in sorted(word_length.keys()):
            occurrences = word_length[length]      # Count occuerrences of words 
            graph = spec_char2 * occurrences       #  make graph
            print(f"{length:3} | {graph.ljust(25)} | {occurrences}")
                                              
    else:
        print("Invalid selection. Terminating the program...")
    
else:
    print("username", valid_user)
    print("password", password)    
    print("unregistered user, terminating the program..")
    

























