import random

def get_names():
    names = []
    while True:
        name = input("Enter a name (or type 'end' to finish): ")
        if name.lower() == 'end':
            break
        names.append(name)
    return names

def select_winner(names):
    if len(names) == 0:
        print("No names entered. Please enter at least one.")
        return
    winner = random.choice(names)
    print(f"The winner is: {winner}")

def run_roulette():
    print("Welcome to the Random Name Roulette!")
    names = get_names()
    select_winner(names