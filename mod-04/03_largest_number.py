number_list = []
while True:
  number = input("Enter a number (or press Enter to quit): ")

  if number == "":
    break

  number_list.append(float(number))

print(F"Smallest number: {min(number_list)}")
print(F"Largest number: {max(number_list)}")
