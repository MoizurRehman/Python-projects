voting_age_in_peturksbouipo: int = 16
voting_age_in_stanlau: int = 25
voting_age_in_mayengua: int = 48

age = int(input("Enter you age "))

if (age >= voting_age_in_peturksbouipo):
    print("You can vote in Peturksbouipo where the voting age is 16")
else:
    print("You can not vote in Peturksbouipo where the voting age is 16")

if (age >= voting_age_in_stanlau):
    print("You can vote in Stanlau where the voting age is 25")
else:
    print("You can not vote in Peturksbouipo where the voting age is 16")

if (age >= voting_age_in_mayengua):
    print("You can vote in Mayengua where the voting age is 48")
else:
    print("You can not vote in Mayengua where the voting age is 48")