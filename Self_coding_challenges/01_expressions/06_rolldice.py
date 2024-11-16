import random

def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f"dice one is {dice1} and dice two is {dice2} and it's sum is {dice1+dice2}")

roll_dice()