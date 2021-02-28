
import random

def game_rules():
    print("          RULES         ")
    print("-------------------------")
    print("For now, this game is rather simple.")
    print("Each player roles the dice, the higher number wins.")
    main_game()
 
def main_game():
    min = 1
    max = 6

    roll = input(f"{player_1}, press 'r' to roll the dice ")
    if roll == 'r' or roll == 'R' or roll == 'roll' or roll == 'Roll':
        num0 = int(random.randint(min,max))
        num1 = int(random.randint(min,max))
        print(num0)
        print(num1)
    else:
        print("This is not a valid input!")

    roll = input(f"{player_2}, press 'r' to roll the dice ")
    if roll == 'r' or roll == 'R' or roll == 'roll' or roll == 'Roll':
        num2 = int(random.randint(min,max))
        num3 = int(random.randint(min,max))
        print(num2)
        print(num3)
    else:
        print("This is not a valid input!")
    
    sol_player_1 = num0 + num1
    sol_player_2 = num2 + num3

    if sol_player_1 > sol_player_2:
        print(f"{player_1} won the game!")
    elif sol_player_1 < sol_player_2: 
        print(f"{player_2} won the game!")
    elif sol_player_1 == sol_player_2:
        print("This was a draw!")

player_1 = input("Input player #1's name")
player_2 = input("Input player #2's name")

rules = input("Do you need to read the rules? y/n ")
if rules ==  'yes' or rules == 'Yes' or rules == 'y' or rules == 'Y':
    game_rules()
else:
    print("Okay, lets play")
    main_game()
    
