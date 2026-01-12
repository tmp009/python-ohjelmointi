import random

code_3_digits = random.randint(0, 9) * 100 + random.randint(0, 9) * 10 + random.randint(0, 9)
code_4_digits = random.randint(1, 6) * 1000 + random.randint(1, 6) * 100 + random.randint(1, 6) * 10 + random.randint(1, 6)

print("3-digit code:", code_3_digits)
print("4-digit code:", code_4_digits)
