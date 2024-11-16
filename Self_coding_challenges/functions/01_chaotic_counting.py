import random
DONE_LIKELIHOOD: float = 0.1

def done():
    if (random.random() < DONE_LIKELIHOOD):
        return True
    return False

def chaotic_counting():
    for i in range(1,11):
        if done():
            break
        print(i)

chaotic_counting()
