
import random

def rules():
    print("For now, this game is rather simple.")
    print("Each player roles the dice, the higher number wins.")
 
def player_one():
    min = 1
    max = 6

    roll = input(f"{player_1}, press 'r' to roll the dice ")
    if roll == 'r' or roll == 'R' or roll == 'roll' or roll == 'Roll':
        print(random.randint(min,max))
        print(random.randint(min,max))
    else:
        print("This is not a valid input!")
    
    player_two()

def player_two():
    min = 1
    max = 6

    roll = input(f"{player_2}, press 'r' to roll the dice ")
    if roll == 'r' or roll == 'R' or roll == 'roll' or roll == 'Roll':
        print(random.randint(min,max))
        print(random.randint(min,max))
    else:
        print("This is not a valid input!")

player_1 = input("Input player #1's name")
player_2 = input("Input player #2's name")

rules = input("Do you need to read the rules? y/n ")
if rules ==  'yes' or rules == 'Yes' or rules == 'y' or rules == 'Y':
    rules()
else:
    print("Okay, lets play")
    player_one()
    
