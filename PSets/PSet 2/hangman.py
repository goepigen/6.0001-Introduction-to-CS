# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_letters = list(secret_word)
    
    letters_guessed_dict = get_letters_guessed_dict(letters_guessed)
    
    for letter in secret_letters:
        try:
            letters_guessed_dict[letter]
        except KeyError:
            return False
    return True


def get_letters_guessed_dict(letters_guessed):
    return { letter: True for letter in letters_guessed}

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    if (is_word_guessed(secret_word, letters_guessed)):
        return list(secret_word)
    
    letters_guessed_dict = get_letters_guessed_dict(letters_guessed)
    
    guessed_word=''
    
    for letter in secret_word:
        try:
            letters_guessed_dict[letter]
            guessed_word = guessed_word + letter
        except KeyError:
            guessed_word = guessed_word + '_ '
            
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    return ''.join([l for l in string.ascii_lowercase if l not in letters_guessed])
    

def print_separator():
    print("--------------------")
    
def print_guesses_left(guesses_left):
    print("You have", guesses_left, "guesses left.")
    
def print_available_letters(letters_guessed):
    print("Available letters:", get_available_letters(letters_guessed))
    
def get_user_guess():
    guess = input("Please guess a letter: ")
    return guess

def is_guess_alphabetic(guess):
    return guess.isalpha()

def warning_update(warnings, guesses_left):
    
    if (warnings>0):
        return [warnings-1, guesses_left]
    
    return [warnings, guesses_left-1]

def is_repeated_guess(guessed_letter, letters_guessed):
    return guessed_letter in letters_guessed

def print_guess_feedback(event, warnings):
    if event == "NOT ALPHA":
        print("Oops! That is  not a valid letter. You have", warnings, "warnings left")
    elif event =="REPEATED GUESS":
        print("Oops! You've already guessed that letter. You have", warnings, "warnings left")
 
    elif event=="GOOD GUESS":
        print("Good guess.")
    elif event=="INCORRECT GUESS":
        print("Oops! That letter is not in my word.")
        
def is_guess_successful(guess, secret_word):
    return guess in secret_word

def is_vowel(letter):
    return letter in ["a","e","i","o","u"]

def get_score(guesses_left, secret_word):
    unique_letters = {a: True for a in secret_word}
    return len(unique_letters.keys())*guesses_left
            

def check_user_guess(secret_word, guess, letters_guessed, warnings, guesses_left, allow_hints=False):
    
    guess_lower = guess.lower()
    
    if (allow_hints and guess_lower=="*"):
        print("Possible word matches are")
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        print("")
        return [warnings, guesses_left, letters_guessed]
    
    if (not is_guess_alphabetic(guess_lower)):
        [updated_warnings, updated_guesses_left] = warning_update(warnings, guesses_left)
        print_guess_feedback("NOT ALPHA", updated_warnings)
        return [updated_warnings, updated_guesses_left, letters_guessed]
    
    if (is_repeated_guess(guess_lower, letters_guessed)):
        [updated_warnings, updated_guesses_left] = warning_update(warnings, guesses_left)
        print_guess_feedback("REPEATED GUESS", updated_warnings)
        return [updated_warnings, updated_guesses_left, letters_guessed]
    
    updated_letters_guessed = letters_guessed + [guess_lower]

    if is_guess_successful(guess_lower, secret_word):
        print_guess_feedback("GOOD GUESS", warnings)
        return [warnings, guesses_left, updated_letters_guessed]
    
    print_guess_feedback("INCORRECT GUESS", warnings)
        
    if is_vowel(guess_lower):
        return [warnings, guesses_left-2, updated_letters_guessed]
    
    return [warnings, guesses_left-1, updated_letters_guessed]
    
def is_game_lost(guesses_left):
    return guesses_left <= 0

def check_end_of_game(guesses_left, secret_word, letters_guessed):
    if is_game_lost(guesses_left):
        print("Sorry, you ran out of guesses. The word was", secret_word+".")
        return True
        
    elif is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your score is", get_score(guesses_left,secret_word))
        return True
    
    return False
    

def hangman(secret_word, allow_hints=False):
    '''
    secret_word: string, the secret word to guess.
    
    '''
    
    print("Welcome to Hangman!")
    
    guesses_left = 6
    warnings = 3
    game_over = False
    letters_guessed=[]
    
    word_length = len(secret_word)
    
    print("I am thinking of a word that is", word_length, "letters long")
    print_separator()
    
    while(not game_over):
        print_guesses_left(guesses_left)
        print_available_letters(letters_guessed)
        current_guess = get_user_guess()
        [warnings, guesses_left, letters_guessed] = check_user_guess(secret_word, 
                                                                     current_guess, 
                                                                     letters_guessed, 
                                                                     warnings, 
                                                                     guesses_left, allow_hints)
        
        game_over = check_end_of_game(guesses_left, secret_word, letters_guessed)
        if not game_over:
            print(get_guessed_word(secret_word, letters_guessed))
            print_separator()
    
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    stripped_my_word = "".join([l.strip() for l in my_word])
    
    if (not len(other_word) == len(stripped_my_word)):
        return False
    
    for i in range(len(stripped_my_word)):
        l = stripped_my_word[i]
        if l == "_" or l == other_word[i] :
            continue
        
        return False
    return True
        
        



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    matches=[]
    
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches.append(word)
    
    if len(matches):
        for word in matches:
            print(word, end=" ")
    else:
        print("No matches found")



def hangman_with_hints(secret_word):
    hangman(secret_word, True)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
