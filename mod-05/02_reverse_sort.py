numbers = []
while True:
  input_number = input("Enter a number: ")

  if not input_number:
    break

  number = float(input_number)
  numbers.append(number)

numbers.sort(reverse=True)

print("The greatest numbers in descending order:")

for number in numbers[0:5]:
  print(number)
