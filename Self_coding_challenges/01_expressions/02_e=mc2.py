def calculate_energy(mass: float) -> float:
    return mass*(299792458*299792458)

mass = float(input("Enter a mass in kg "))
print(f"Energy of Mass = {mass}kg as per Einstein formula E=mc** is = {calculate_energy(mass)}joules")