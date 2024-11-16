affirmation: str = "I am capable of doing anything I put my mind to."

user_affirmation = input("Enter a affirmation ")

while (affirmation != user_affirmation):
    print("That was not the affirmation.")
    user_affirmation = input("Enter a affirmation ")

print("That's right!")