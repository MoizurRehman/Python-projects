min_height_for_ride = 50
height = input("Enter your height ")

while(height):
    if (int(height) >= min_height_for_ride):
     print("You're tall enough to ride!")
    else:
     print("You're not tall enough to ride, but maybe next year!")
    height = input("Enter your height ")
