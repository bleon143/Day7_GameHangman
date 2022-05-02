## IMPORT MODULES
import random
import os

## DECLARE VARIABLES

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]

## BEGIN DEFINE FUNCTIONS

## BEGIN DEFINE FUNCTION
def fn_ClearScreen():

   ## FOR WINDOWS
   if os.name == 'nt':    
      _ = os.system('cls')

   ## FOR MAC AND LINUX
   elif os.name == 'posix':
      _ = os.system('clear')

   ## TEST PRINT OUTPUT
   ## print(os.name)
   ## print(os.system)

## END DEFINE FUNCTION

## BEGIN DEFINE FUNCTION
def fn_GetWord(word_list):

    ## DECLARE VARIABLES
    ListOfWords = word_list ## ListOfWords = ["aardvark", "baboon", "camel"]

    ## CHOOSE RANDOM WORD FROM LIST OF WORDS ; CONVERT TYPE TEXT STRING TO TYPE LIST
    WordSelected = list(random.choice(ListOfWords))

    ## TEST PRINT OUTPUT
    print("\n")
    ## print(f'Pssst, the hidden, mystery word solution is {WordSelected}.')
    print(f'Pssst, the hidden, mystery word solution can be made visible by uncommenting the code.')

    ## RETURN
    return(WordSelected) ## RETURNS TEXT STRING

## END DEFINE FUNCTION

## BEGIN DEFINE FUNCTION
def fn_DisplayWord(WordSelected):

    ## DECLARE VARIABLES
    WordDisplay = [] ## EMPTY LIST

    ## COUNT LENGTH OF THE WORD SELECTED
    NumberOfLettersInWord = len(WordSelected)

    ## BEGIN FOR LOOP
    for each in range(NumberOfLettersInWord):

        WordDisplay += "_"

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print("\n")
    print(f"Guess the {NumberOfLettersInWord} letters of the hidden, mystery word; You have a total of 6 lives:")
    print("\n")
    print(WordDisplay)

    ## RETURN
    return(WordDisplay) ## RETURNS LIST OF SPACES

## END DEFINE FUNCTION

## BEGIN DEFINE FUNCTION
def fn_GetUserInput(ListOfGuesses):

    ## ASK USER TO GUESS A LETTER
    print("\n")
    UserInput = input(f"Guess a letter:\n").lower()

    ## CLEAR SCREEN
    _ = fn_ClearScreen()

    ## IF GUESSED LETTER IS IN THE LIST OF GUESSES,
    if UserInput in ListOfGuesses:
        
        ## THEN DO NOTHING
        print("\n")
        print(f"You've already guessed the letter {UserInput}, but you still lose a life!")

    ## OTHERWISE APPEND THAT LETTER TO THE LIST OF GUESSES
    else:
        ListOfGuesses.append(UserInput)

    ## RETURN
    return(UserInput, ListOfGuesses) ## RETURNS TEXT STRING CHARACTER LETTER; LIST OF GUESSES

## END DEFINE FUNCTION

## BEGIN DEFINE FUNCTION
def fn_CheckLettersInWord(WordSelected, WordDisplay, UserInput):

    ## DECLARE VARIABLES
    ## SET INITIAL VALUE TO FALSE
    IsLetterInWord = False
    
    ## GET LENGTH OF WORD SELECTED
    LengthOfWord = len(WordSelected)

    ## CHECK IF USER INPUT GUESS OF LETTER IS WITHIN THE WORD SELECTED; UPDATE WORDDISPLAY

    ## BEGIN FOR LOOP
    for EachIndex in range(LengthOfWord):
        
        ## IF THE LETTER FOUND IN THE MYSTERY WORD MATCHES USER INPUT,
        if WordSelected[EachIndex] == UserInput:
            
            ## TEST PRINT OUTPUT
            ## print("\n")
            ## print("TRUE")

            ## THEN CHANGE THAT BLANK SPACE IN WORD DISPLAY TO BE THE LETTER OF USER INPUT
            WordDisplay[EachIndex] = UserInput

            ## TEST PRINT OUTPUT
            ## print(f"Current position: {EachIndex}\n Current letter: {WordSelected[EachIndex]}\n Guessed letter: {UserInput}")

            ## IF LETTER FOUND, SET STATUS OF IsLetterInWord TO TRUE
            IsLetterInWord = True


        else:

            ## TEST PRINT OUTPUT
            ## print("\n")
            ## print("FALSE")

            ## IF LETTER NOT FOUND, KEEP DEFAULT STATUS OF IsLetterInWord TO FALSE
            
            pass

    ## END FOR LOOP

    ## RETURN
    return(WordDisplay, IsLetterInWord)

## END DEFINE FUNCTION

## BEGIN DEFINE FUNCTION

def fn_SetGameStatus(WordSelected, UserInput, IsLetterInWord, NumberOfLives):

    ## IF LETTER FOUND IN WORD, THEN ALL OK; CONTINUE GAME
    if IsLetterInWord == True:

        ## GAME NOT OVER
        IsGameOver = False

    ## ELSE IF LETTER NOT FOUND IN WORD, THEN PLAYER LOSES A LIFE
    elif IsLetterInWord == False:

        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print("\n")
        print(f"The letter {UserInput} is not in the hidden, mystery word.")
   
        ## USER LOSES A LIFE
        NumberOfLives -= 1

        ## IF NUMBER OF LIVES == 0, THEN GAME OVER
        if NumberOfLives == 0:

            print("\n")
            print(f"You Lose. The word was {WordSelected}")

            ## GAME OVER - WIN OR LOSE
            IsGameOver = True

        else:

            ## GAME NOT OVER
            IsGameOver = False

    ## RETURN
    return(IsGameOver, NumberOfLives)

## END DEFINE FUNCTION

## BEGIN DEFINE FUNCTION
def fn_CheckIfBlanks(WordStatus, IsGameOver):
    
    if "_" not in WordStatus:

        ## TEST PRINT OUTPUT
        print("\n")
        print("Congratulations! Mazal Tov! You Win!")

        ## GAME OVER - WIN OR LOSE
        IsGameOver = True

    else:

        print("Game not yet over... keep guessing!")

    ## RETURN
    return(IsGameOver)

## END DEFINE FUNCTION

## END DEFINE FUNCTIONS