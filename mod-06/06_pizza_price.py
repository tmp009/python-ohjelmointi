import math

def calculate_unit_price(diameter, price=1):
    radius = diameter / 2
    area_cm2 = math.pi * (radius ** 2)
    area_m2 = area_cm2 / 10000
    if area_m2 == 0:
        return 0
    unit_price = price / area_m2
    return unit_price


first_input_diameter = float(input("Enter the diameter of the first pizza (cm): "))
first_price = float(input("Enter the price of the first pizza (euros): "))
second_input_diameter = float(input("Enter the diameter of the second pizza (cm): "))
second_price = float(input("Enter the price of the second pizza (euros): "))

first_unit_price = calculate_unit_price(first_input_diameter, first_price)
second_unit_price = calculate_unit_price(second_input_diameter, second_price)

print(f"Unit price of the first pizza: {first_unit_price:.2f} euros/m²")
print(f"Unit price of the second pizza: {second_unit_price:.2f} euros/m²")

if first_unit_price < second_unit_price:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")
