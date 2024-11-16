fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
total_amount = 0

for name, price in fruits.items():
    quantity = int(input(f"How many {name} you wnat to buy? "))
    total_amount = total_amount + (price*quantity)

print(f"Totla amount is {total_amount}")