import random

print("Rock Paper Scissors")
choices = ["rock", "paper", "scissors"]

user = input("your choice (r / p / s): ").lower()
computer = random.choice(choices)

def winer(user, computer):
    status = ''

    if computer == 'rock':
        if user == 'r':
            status == "Draw"
        elif user == 'p':
            status = 'win'
        elif user == 's':
            status = 'lose'

    elif computer == 'paper':
        if user == 'p':
            status == "Draw"
        elif user == 's':
            status = 'win'
        elif user == 'r':
            status = 'lose'

    elif computer == 'scissors':
        if user == 's':
            status == "Draw"
        elif user == 'p':
            status = 'lose'
        elif user == 'r':
            status = 'win'

    return status

status = winer(user, computer)
print(f'computer choose "{computer}"')
if status == 'win':
    print("You won!")
elif status == 'lose':
    print("You lost!")
elif status == 'draw':
    print("Draw!")