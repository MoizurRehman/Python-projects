def sum_of_list(numbers: list) -> int:
    sum = 0
    for number in numbers:
        sum = sum + number
    
    return sum

numbers = [1,2,3,4,5]

print(f"Sum of all theses number {numbers} is {sum_of_list(numbers)}")