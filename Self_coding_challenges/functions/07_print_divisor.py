def print_divisor(num: int) -> list:
    result = []
    for i in range(1,int(num/2)):
        if (num % i == 0):
            result.append(i)
    return result
        

num = int(input("Enter a number: "))
print(f"The divisors of {num} is {print_divisor(num)}")