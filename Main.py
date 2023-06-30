import random

def play(): 
    user = input("'r' for rock, 'p' for apper, 's' for scissors: ")
    computer_choice = random.choice(['r', 'p', 's'])
    print(f"{computer_choice}")
    if user == computer_choice: 
        return "Tie"
    if is_win(user, computer_choice):
        return "You won!"
        
    return "Computer won!"
    
def is_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True
    else:
        return False

print(f"{play()}")