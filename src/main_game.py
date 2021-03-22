
import random
from src.color_class import bcolors

def intro():
    rules = input("Do you need to read the rules? y/n ")
    if rules ==  'y' or rules == ' y':
        game_rules()
    elif rules == 'n' or rules == ' n':
        print("Okay, lets play")
        main_game()
    while rules != 'y' and rules != ' y' and rules != 'n' and rules != ' n':
        print(bcolors.FAIL + "NOT VALID!" + bcolors.ENDC)
        return intro()

def game_rules():
    print("               RULES         ")
    print("-------------------------------------")
    print("For now, this game is rather simple.")
    print("Each player roles the dice, the higher number wins.")
    print("-------------------------------------")
    main_game()
 
def main_game():
    min = 1
    max = 6

    player_1 = input("Input player #1's name")
    player_2 = input("Input player #2's name")

    roll = input(f"{player_1}, press 'r' to roll the dice ")
    if roll == 'r':
        num0 = int(random.randint(min,max))
        num1 = int(random.randint(min,max))
        print(num0)
        print(num1)
    while roll != 'r':
        print(bcolors.FAIL + "This is not a valid input!" + bcolors.ENDC)
        roll = input("Press 'r' to roll the dice again.")
        if roll == 'r':
            num0 = int(random.randint(min,max))
            num1 = int(random.randint(min,max))
            print(num0)
            print(num1)
            

    roll = input(f"{player_2}, press 'r' to roll the dice ")
    if roll == 'r':
        num2 = int(random.randint(min,max))
        num3 = int(random.randint(min,max))
        print(num2)
        print(num3)
    while roll != 'r':
        print(bcolors.FAIL + "This is not a valid input!" + bcolors.ENDC)
        roll = input("Press 'r' to roll the dice again.")
        if roll == 'r':
            num2 = int(random.randint(min,max))
            num3 = int(random.randint(min,max))
            print(num2)
            print(num3)
    
    sol_player_1 = num0 + num1
    sol_player_2 = num2 + num3

    if sol_player_1 > sol_player_2:
        print(bcolors.OKGREEN + player_1.upper() + " WON THE GAME!" + bcolors.ENDC)
    elif sol_player_1 < sol_player_2: 
        print(bcolors.OKGREEN + player_2.upper() + " WON THE GAME!" + bcolors.ENDC)
    elif sol_player_1 == sol_player_2:
        print("This was a draw!")

def play_again():
    q =  input("Would you like to play again? y/n ")
    if q == 'y' or q == ' y':
        main_game()
    elif q == 'n' or q == ' n':
        print("Thank you for visitng my program")
    while q != 'y' and q != ' y' and q != 'n' and q != ' n':
        print(bcolors.FAIL + "NOT VALID." + bcolors.ENDC)
        return play_again()

intro()
play_again()