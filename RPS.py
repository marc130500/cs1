import random
def get_user_choice():
    user_choice = input("Choose Rock, Paper, Scissors: ").strip().lower()
    while user_choice not in ['rock','paper','scissors']:
        print('invalid choice. Please try again.')
        user_choice = input('Choose Rock, Paper, Scissors').strip().lower():
            return user_choice
        
        def get_computer_choice():
            return random.choice(['rock'
        
