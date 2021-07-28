
import random
from .color_class import bcolors
from .dice_class import Dice

def main_game():

    player_1 = input("Input player #1's name: ")
    player_2 = input("Input player #2's name: ")
    die_roll = Dice(1,6)
    roll = input(f"{player_1}, press 'r' to roll the dice ")
    if roll == 'r':
        num0 = die_roll.roll_dice1()
        num1 = die_roll.roll_dice2()
        print(num0)
        print(num1)
    while roll != 'r':
        print(bcolors.FAIL + "This is not a valid input!" + bcolors.ENDC)
        roll = input("Press 'r' to roll the dice again.")
        if roll == 'r':
            num0 = die_roll.roll_dice1()
            num1 = die_roll.roll_dice2()
            print(num0)
            print(num1)
            

    roll = input(f"{player_2}, press 'r' to roll the dice ")
    if roll == 'r':
        num2 = die_roll.roll_dice1()
        num3 = die_roll.roll_dice2()
        print(num2)
        print(num3)
    while roll != 'r':
        print(bcolors.FAIL + "This is not a valid input!" + bcolors.ENDC)
        roll = input("Press 'r' to roll the dice again.")
        if roll == 'r':
            num2 = die_roll.roll_dice1()
            num3 = die_roll.roll_dice2()
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