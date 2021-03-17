
from .game import main_game
from .color_class import bcolors

def play_again():
    q =  input("Would you like to play again? y/n ")
    if q == 'y' or q == ' y':
        main_game()
    elif q == 'n' or q == ' n':
        print("Thank you for visitng my program")
    while q != 'y' and q != ' y' and q != 'n' and q != ' n':
        print(bcolors.FAIL + "NOT VALID." + bcolors.ENDC)
        return play_again()
