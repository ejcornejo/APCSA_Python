#File: hangman.py
#Student: Esteban Cornejo
#
#Date: October 4, 2024
#Description of Program: This program is a part of an assignment that lets the user play a game of hangman.
#GitHub: ejcornejo
import random

wrds = ["python", "programming", "computer", "hangman", "loops", "functions", "conditionals", "boolean"]

def choose_word(wrds):
    return random.choice(wrds)

def display_word(word, guesses):
    print(" ".join([letter if letter in guesses else "_" for letter in word]))

def get_guesses():
    guess = input("Enter a letter: ").lower()
    return guess

def hangman():
    print("Welcome to Hangman!")
    guesses = []
    correct = 0
    i = 0
    word = choose_word(wrds)
    
    while i < 6 and correct == 0:
        display_word(word, guesses)
        print(f"Incorrect guesses left: {6 - i}")
        
        guess = get_guesses()

        if guess in guesses:
            print("You've already guessed that letter.")
        else:
            guesses.append(guess)
            if guess in word:
                if all(letter in guesses for letter in word):
                    correct = 1
            else:
                i += 1
    
    if correct == 1:
        print(f"Congratulations! You've guessed the word '{word}'!")
    else:
        print(f"You've run out of guesses! The word was '{word}'.")

hangman()
