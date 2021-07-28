

import random

class Dice:
    
    def __init__(self, min, max):
        self.min = min
        self.max = max
        
    def roll_dice1(self):
        dice1 = int(random.randint(self.min, self.max))
        return dice1
    
    def roll_dice2(self):
        dice2 = int(random.randint(self.min, self.max))
        return dice2