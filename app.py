# Create Rock, Paper, Scissors game

# Importing the random module
import random

# Create list of possible choices
choices = ['r', 'p', 's']

# Create score and rounds played variables
user_score = 0
computer_score = 0
rounds_played = 0

# Function to check if the user wins
def is_user_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True

    return False

# Function to check if computer wins
def is_computer_win(user, computer):
    if (computer == 'r' and user == 's') or (computer == 's' and user == 'p') or (computer == 'p' and user == 'r'):
        return True

    return False

# Function to check if it's a tie
def is_tie(user, computer):
    if user == computer:
        return True

    return False



# Function to print the score and rounds played
def print_score(user_score, computer_score, rounds_played):
    print(f'User score: {user_score}')
    print(f'Computer score: {computer_score}')
    print(f'Rounds played: {rounds_played}')

# Function to print welcome message
def print_welcome():
    print('Welcome to Rock, Paper, Scissors game!')

# Function to print rules
def print_rules():
    print('Rules:')
    print('Rock beats Scissors')
    print('Scissors beats Paper')
    print('Paper beats Rock')


# Funtion to print goodbye message
def print_goodbye():
    print('Goodbye!')

# Function to print user and computer choices
def print_choices(user, computer):
    print(f'User choice: {user}')
    print(f'Computer choice: {computer}')


print_welcome()
print_rules()
# Create the loop to play the game
while True:
    # Play the game
       # User input
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    # Computer input
    computer = random.choice(['r', 'p', 's'])

    # If the user and computer choices are the same
    if is_tie(user,computer):
         print('It\'s a tie')
         rounds_played += 1

    # If the user wins
    if is_user_win(user, computer):
         print('You won!')
         user_score += 1

    # If the computer wins
    if is_computer_win(user, computer):
         print('You lost!')
         computer_score += 1
    

    rounds_played += 1


    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != 'y':
        print_score(user_score, computer_score, rounds_played)
        print_choices(user, computer)
        print_goodbye()
        break
    





