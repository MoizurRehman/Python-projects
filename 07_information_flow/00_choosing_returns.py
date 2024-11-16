ADULT_AGE: int = 18
def is_adult(age):
    if age >= ADULT_AGE:
        return True
    return False

age: int = int(input("Enter a age "))
print(is_adult(age))