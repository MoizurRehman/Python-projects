all_numbers: list = []
number = input("Enter a number ")

while (number):
    all_numbers.append(int(number))
    number = input("Enter a number ")

def convert_to_dictionary(numbers: list):
    all_numbers_count = {}
    for num in numbers:
        if num not in all_numbers_count:
            all_numbers_count[num] = 1
        else:
            all_numbers_count[num] = all_numbers_count[num] + 1
    return all_numbers_count
num_dic = convert_to_dictionary(all_numbers)
for key, value in num_dic.items():
    print(f"{key} appears {value} times.")