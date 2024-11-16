phone_book = {}

while True:
    name = input("Enter a name ")
    if not name:
        break
    number = input("Enter a number")
    phone_book[name] = number

print(phone_book)