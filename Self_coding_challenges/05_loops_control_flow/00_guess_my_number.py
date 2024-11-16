import random

guess_number = random.randint(1,99)

user_number = int(input("Enter a guess "))

while(guess_number != int(user_number)):
    if (guess_number > int(user_number)):
        print("Your guess is too low")
    else:
         print("Your guess is too heigh")
    user_number = input("Enter a guess ")

print(f"Congrats! The number was: {user_number}")