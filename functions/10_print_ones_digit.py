def print_ones_digit(num: int):
    return num % 10

number = int(input("Enter a number "))
print(f"Last number of {number} is {print_ones_digit(number)}")