import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("Enter number of sides for the dice: "))

while True:
    roll = roll_dice(sides)
    print(roll)
    if roll == sides:
        break
