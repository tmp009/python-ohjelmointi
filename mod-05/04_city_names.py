cities = []

for _ in range(5):
  city_name = input("Enter the name of a city: ")
  cities.append(city_name)

print("\n\nThe cities you entered:")
for city in cities:
  print(city)
