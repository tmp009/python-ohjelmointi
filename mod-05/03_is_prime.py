input_number = int(input("Enter an integer: "))

if input_number <= 1:
    print(f"{input_number} is not a prime number.")

else:
  for divisor in range(2, input_number):

    if input_number % divisor == 0:
      print(f"{input_number} is not a prime number.")
      break
  else:
      print(f"{input_number} is a prime number.")
