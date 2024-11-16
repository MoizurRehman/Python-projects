import math
def get_hypotenuse(base: int, perpendicular: int) -> int:
    return math.sqrt(base**2 + perpendicular** 2)

base = int(input("Enter a length of base of triangel "))
perpendicular = int(input("Enter a length of perpendicular of triangel "))

print(f"Length of Hypotenuse of triangle is = {get_hypotenuse(base, perpendicular)}")