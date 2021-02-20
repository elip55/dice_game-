import random 
def main_code():
    min = 1
    max = 6
    roll = input("Press 'r' to roll the dice ")
    if roll == 'r' or roll == 'R' or roll == 'roll' or roll == 'Roll':
        print(random.randint(min,max))
        print(random.randint(min,max))
    answer = input("Would you like to roll again?")
    while answer == 'yes' or answer == 'Yes':
        main_code()
        break
    else: 
        print("Thank you for visiting my program!")

main_code()