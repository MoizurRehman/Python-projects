numbers: list[int] = [1, 2, 3, 4]
i: int = 0

while(i < len(numbers)):
    numbers[i] = numbers[i] ** 2
    i = i + 1

print(numbers)
