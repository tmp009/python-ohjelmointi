def gallons_to_liters(gallons):
    litres = gallons * 3.785
    return litres

while True:
    gallons_input = float(input("Enter a volume in American gallons (negative value to quit): "))

    if gallons_input < 0:
      print("Program finished.")
      break

    litres_output = gallons_to_liters(gallons_input)
    print(f"{gallons_input} American gallons is {litres_output:.2f} liters.")
