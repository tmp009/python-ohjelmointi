import random

rolls = int(input("How many dice to roll: "))
rolled = []
for roll in range(rolls):
  die_result = random.randint(1, 6)
  rolled.append(die_result)

print("Sum of the dice:", sum(rolled))
