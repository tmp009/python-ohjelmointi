talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

LOT = 13.3
POUND = LOT * 32
TALENT = POUND * 20

total_grams = talents * TALENT + pounds * POUND + lots * LOT
kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000

print(f"The weight in modern units:\n{kilograms} kilograms and {remaining_grams:.2f} grams.")
