import random
import string
from words import words

def valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def game():
    my_word = valid_word(words)
    lives = len(my_word)*2
    letters_in_computer_word = set(my_word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    while len(letters_in_computer_word) > 0 and lives > 0:
        print(f"You've already used those letters: ", "".join(used_letters))
        print(f"Lives left: {lives}")
        my_response = (letter if letter in used_letters else "-"for letter in my_word)
        t = ("".join(my_response))
        print(t)
        guess_of_letter = input("Choose your letter: ").upper()
        if guess_of_letter in alphabet:
            if guess_of_letter in letters_in_computer_word:
                letters_in_computer_word.remove(guess_of_letter)
                print(f"You was correct letter {guess_of_letter} is in the word.")
            else:
                print(f"You was incorrect letter {guess_of_letter} is not in the word.")
                lives -= 1
            used_letters.add(guess_of_letter)
        elif guess_of_letter in used_letters:
            print(f"You've already used letter {guess_of_letter} once. Retake your try.")
        else:
            print("You did something wrong. Try to do it once more.")
    if len(letters_in_computer_word) == 0:
        print(f"You won the game your word was {my_word}")
    else:
        print(f"You didn't win this time, your word was {my_word}, your final answer was {t}")


valid_word(words)
game()
