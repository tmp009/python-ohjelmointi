
def get_season(month_number):
  winter = [12, 1, 2]
  spring = [3, 4, 5]
  summer = [6, 7, 8]
  autumn = [9, 10, 11]

  if month_number in winter:
    return "winter"
  elif month_number in spring:
    return "spring"
  elif month_number in summer:
    return "summer"
  elif month_number in autumn:
    return "autumn"
  else:
    return None


month = int(input("Enter the number of a month (1-12): "))
season = get_season(month)

print(f"You entered: {month}")

if season is None:
  print("Please enter a number between 1 and 12.")
else:
  print(f"The season is {season}.")
