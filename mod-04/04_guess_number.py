import random

random_number = random.randint(1, 10)

while True:
  number = int(input("Guess a number (1-10): "))

  if number == random_number:
    print("Correct")
    break

  elif number < random_number:
    print("Too low")
  else:
    print("Too high")
