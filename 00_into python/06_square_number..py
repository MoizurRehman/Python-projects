def findSqare(number: int) -> int:
    return number*number

number: int = int(input("Enter a number "))

print(f"{number} squared is {findSqare(number)}")