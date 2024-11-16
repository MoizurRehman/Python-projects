def convert_foot_to_inch(foot: float) -> float:
    return foot*12

foot = float(input("Enter a number in foot"))
print(f"Tool inch in {foot} foot is {convert_foot_to_inch(foot)}")