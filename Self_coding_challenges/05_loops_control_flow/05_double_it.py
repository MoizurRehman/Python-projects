number: int = int(input("Enter a number "))

while (True):
    number = number + number
    print(number)
    if (number >= 100):
        break
