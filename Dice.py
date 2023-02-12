import random

class Dice:
    def rollDice():
        return random.randint(1,6)
    
    print(rollDice() + rollDice())