def count_even(list: list):
    for i in range(len(list)):
        if (i % 2 != 0):
            print(i)


all_numbers: list = []

number = input("Enter a number ")

while(number):
    all_numbers.append(int(number))
    number = input("Enter a number ")

count_even(all_numbers)