current_value = 0
next_value = 1

while (current_value <= 20):
    print(current_value)
    value_after_next = current_value + next_value
    current_value = next_value
    next_value = value_after_next