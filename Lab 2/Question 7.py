"""
Word guessing game (hangman)
○ A list of words will be hardcoded in your program, out of which the interpreter will
○ choose 1 random word.
○ The user first must input their names
○ Ask the user to guess any alphabet. If the random word contains that alphabet, it
○ will be shown as the output(with correct placement)
○ Else the program will ask you to guess another alphabet.
○ Give 7 turns maximum to guess the complete word.
"""

import random

playername = input("What is your name? :  ")
print(f"Good Luck {playername} ^__^")

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']
word = random.choice(words)

print("Guess the characters")
guesses = ''
turns = 7
while turns > 0:
    failed = len(word)
    for char in word:
        if char in guesses:
            print(char, end=" ")
            failed -= 1
        else:
           print("_")

    if failed == 0:
        print("\n")
        print(f"The word is: {word}")
        print(f"You Win {playername}")

        break

    print()
    guess = input(" Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong !!")
        print("You have", + turns, 'more guesses !!')
        if turns == 0:
            print(f"You Loose {playername} ")