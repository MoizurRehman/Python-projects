max_length: int = 2
numbers: list = [1,23,4,5,6,7.6,890]

while(len(numbers) > max_length):
    print(numbers.pop())

print(numbers)