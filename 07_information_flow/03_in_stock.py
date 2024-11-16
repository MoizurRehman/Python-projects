def num_in_stock(fruit: str):
    all_fruits_stocks: dict = {
        "apple": 4,
        "orange": 5,
        "bannana": 43,
        "graphs": 32
    }
    if (fruit in all_fruits_stocks):
        return all_fruits_stocks[fruit]
    return 0

fruit = input("Enter a fruit ")
print(f"Total stock of {fruit} is {num_in_stock(fruit)}")