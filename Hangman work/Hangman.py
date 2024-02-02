import random
from words import words
from hangman_visual import lives_visual_dict
import string

#This function in take a list of words and randomize it 
def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)

    lives = 7

    #Loop when the len is not finish and the lives did not end

        #Show out much lives are left and how many letters been used

        #for every letter in the word, if a letter is correct then place it otherwise '-'
        # word_list = [letter if letter in used_letters else '-' for letter in word]

        #print the number of lives along with the visual
        #print out the current status on the word

        #ask the user for a letter and set it upper
        #check if the letter enter is a letter
        #check if the letter is already used
        #check if the letter is in the word letters

    # gets here when len(word_letters) == 0 OR when lives == 0


if __name__ == '__main__':
    hangman()