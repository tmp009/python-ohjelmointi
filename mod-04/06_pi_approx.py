import random

max_loops = int(input("Enter iteration count: "))

inside_circle = 0
count = 0

while True:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x * x + y * y < 1:
        inside_circle += 1

    count += 1

    if count >= max_loops:
        break

pi_estimate = 4 * inside_circle / max_loops
print(f"Approximation of pi: {pi_estimate}")
