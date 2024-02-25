#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = '''
      _,---.                  ,----.    ,-,--.    ,-,--.   .=-.-. 
  _.='.'-,  \ .--.-. .-.-. ,-.--` , \ ,-.'-  _\ ,-.'-  _\ /==/_ / 
 /==.'-     //==/ -|/=/  ||==|-  _.-`/==/_ ,_.'/==/_ ,_.'|==|, |  
/==/ -   .-' |==| ,||=| -||==|   `.-.\==\  \   \==\  \   |==|  |  
|==|_   /_,-.|==|- | =/  /==/_ ,    / \==\ -\   \==\ -\  /==/. /  
|==|  , \_.' )==|,  \/ - |==|    .-'  _\==\ ,\  _\==\ ,\ `--`-`   
\==\-  ,    (|==|-   ,   /==|_  ,`-._/==/\/ _ |/==/\/ _ | .=.     
 /==/ _  ,  //==/ , _  .'/==/ ,     /\==\ - , /\==\ - , /:=; :    
 `--`------' `--`..---'  `--`-----``  `--`---'  `--`---'  `=`     
'''

# Import modules - random for random number generation
import random

# Create function to generate random number between 1 and 100
def generate_number():
    '''Generate random number between 1 and 100'''
    return random.randint(1,100)

# Create function to check user guess against random number
def check_guess(user_guess, random_number):
    '''Check user guess against random number'''
    if user_guess > random_number:
        return "Too high."
    elif user_guess < random_number:
        return "Too low."
    else:
        return "You got it!"

# Create function to check difficulty level
def check_difficulty(difficulty):
    '''Check difficulty level and return number of attempts'''
    if difficulty == "easy":
        return 10
    else:
        return 5

# Create function to play game
def play_game():
    # print logo
    print(logo)
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = check_difficulty(difficulty)
    print(f"You have {attempts} attempts remaining to guess the number.")
    
    # Generate random number
    random_number = generate_number()
    
    # Loop through attempts
    while attempts > 0:
        # Get user guess
        user_guess = int(input("Make a guess: "))
        # Check user guess
        print(check_guess(user_guess, random_number))
        # Check if user guess is correct
        if user_guess == random_number:
            return
        # Decrement attempts
        attempts -= 1
        # Print attempts remaining
        print(f"You have {attempts} attempts remaining to guess the number.")

# Create function to run game
def run_game():
    play_game()
    while input("Do you want to play again? Type 'y' or 'n': ") == "y":
        # clear
        play_game()