## DAY 7
## 100 DAYS OF PYTHON
## https://100daysofpython.dev/

## PYTHON GAME: Hangman
## CODE START:  https://replit.com/@appbrewery/Day-7-Hangman-1-Start
## CODE END:  https://replit.com/@appbrewery/Day-7-Hangman-Final

## IMPORT MODULES
import mod_hangman

## DECLARE VARIABLES
IsGameOver = False
NumberOfLives = 6
ListOfGuesses = []

## BEGIN MAIN PROGRAM
## CLEAR SCREEN
_ = mod_hangman.fn_ClearScreen()

## PRINT GAME LOGO
PrintGameLogo = print(mod_hangman.logo)

## CALL FUNCTION
WordSelected = mod_hangman.fn_GetWord(mod_hangman.word_list) ## RETURNS TEXT STRING

## CALL FUNCTION
WordDisplay = mod_hangman.fn_DisplayWord(WordSelected) ## RETURNS LIST OF SPACES

## TEST PRINT OUTPUT
## print(f"WordSelected = {WordSelected}")
## print(f"WordDisplay = {WordDisplay}")

## INFINITE WHILE GAME LOOP UNTIL USER WINS OR LOSES
while not IsGameOver: ## IsGameOver == False:

    ## CALL FUNCTION
    UserInput, ListOfGuesses = mod_hangman.fn_GetUserInput(ListOfGuesses)

    ## CALL FUNCTION
    WordStatus, IsLetterInWord = mod_hangman.fn_CheckLettersInWord(WordSelected, WordDisplay, UserInput)

    ## TEST PRINT OUTPUT
    ## print("\n")
    ## print(f"WordDisplay = {WordDisplay}")
    ## print(type(WordDisplay))

    ## TEST PRINT OUTPUT
    ## print("\n")
    ## print(f"WordStatus = {WordStatus}")
    ## print(type(WordStatus))

    ## TEST PRINT OUTPUT
    ## print("\n")
    ## print(f"IsLetterInWord = {IsLetterInWord}")
    ## print(type(IsLetterInWord))

    ## CALL FUNCTION
    IsGameOver, NumberOfLives = mod_hangman.fn_SetGameStatus(WordSelected, UserInput, IsLetterInWord, NumberOfLives)
    
    ## JOIN ELEMENTS OF THE LIST; CONVERT TO TEXT STRING
    WordSelectedAsString = ' '.join(WordSelected)

    ## JOIN ELEMENTS OF THE LIST; CONVERT TO TEXT STRING
    WordDisplayAsString = ' '.join(WordDisplay)

    ## JOIN ELEMENTS OF THE LIST; CONVERT TO TEXT STRING
    WordStatusAsString = ' '.join(WordStatus)

    ## JOIN ELEMENTS OF THE LIST; CONVERT TO TEXT STRING
    ListOfGuessesAsString = ' '.join(ListOfGuesses)

    ## TEST PRINT OUTPUT
    ## print("\n")
    ## print(f"WordSelectedAsString = {WordSelectedAsString}")
    ## print("\n")
    ## print(f"WordDisplayAsString = {WordDisplayAsString}")
    print("\n")
    print(f"WordStatusAsString = {WordStatusAsString}")
    print("\n")
    print(f"List of Guesses so far: {ListOfGuessesAsString}")
    print("\n")
    print(f"You have {NumberOfLives} of lives remaining.")

    ## TEST PRINT OUTPUT
    print(mod_hangman.stages[NumberOfLives])

    ## CALL FUNCTION
    GameStatus = mod_hangman.fn_CheckIfBlanks(WordStatus, IsGameOver)

    ## CHECK AND SET GAME STATUS BEFORE NEXT ROUND OF WHILE LOOP
    IsGameStatus = GameStatus

## TEST PRINT OUTPUT
print("\n")
print("GAME OVER")
print("\n")

## END MAIN PROGRAM



