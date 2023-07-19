import random
import string

passwords = ["oko", "dom"]
word = passwords[random.randrange(0,len(passwords))]
word_len = len(word)
word_elements = list(word)
guess_word = []
win_word = ""
for element in word_elements:
    guess_word.append("_")

def check_the_guess2(guess_letter):
    for index, element in enumerate(word_elements):
        if element == guess_letter:
            guess_word[index] = guess_letter
    return guess_word

def check_user_input(letter):
    if letter.isalpha():
        return False
    else:
        return True

chances = word_len + 2

while chances > 0:
    if word_elements == guess_word:
        separator = ""
        win_word = separator.join(guess_word)
        break
    else:
        guess_letter = input("enter a letter")
        while check_user_input(guess_letter):
            guess_letter = input("enter a letter")
        check_the_guess2(guess_letter)
        print(guess_word)
        chances -= 1

if win_word == word:
    print("congratulations you guessed the password :", win_word)
else:
    print("You lose")