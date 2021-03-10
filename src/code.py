
import random


def intro():
    rules = input("Do you need to read the rules? y/n ")
    if rules ==  'yes' or rules == 'Yes' or rules == 'y' or rules == 'Y':
        game_rules()
    else:
        print("Okay, lets play")
        main_game()

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
        print("This is not a valid input!")
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
        print("This is not a valid input!")
        roll = input("Press 'r' to roll the dice again.")
        if roll == 'r':
            num2 = int(random.randint(min,max))
            num3 = int(random.randint(min,max))
            print(num2)
            print(num3)
    
    sol_player_1 = num0 + num1
    sol_player_2 = num2 + num3

    if sol_player_1 > sol_player_2:
        plyr_1_win = player_1.upper() + " WON THE GAME!"
        print(plyr_1_win)
    elif sol_player_1 < sol_player_2: 
        plyr_2_win = player_2.upper() + " WON THE GAME!"
        print(plyr_2_win)
    elif sol_player_1 == sol_player_2:
        print("This was a draw!")

def play_again():
    q =  input("Would you like to play again? y/n ")
    if q == 'y' or q == ' y' or q == 'Y' or q == ' Y':
        main_game()
    elif q == 'n' or q == 'N' or q == 'no':
        print("Thank you for visitng my program")

intro()
play_again()