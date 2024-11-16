import random

def two_dice_result() -> int:
    return random.randint(1,6) + random.randint(1,6)

print(two_dice_result())