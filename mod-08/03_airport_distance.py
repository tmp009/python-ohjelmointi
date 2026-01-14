import mysql.connector
from geopy.distance import geodesic
def get_airport_coordinates(icao_code):
    db_con = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        password="password",
        autocommit=True
    )

    cursor = db_con.cursor()
    query = """
        SELECT longitude_deg, latitude_deg FROM airport
        WHERE ident = %s
    """
    cursor.execute(query, (icao_code,))
    rows = cursor.fetchone()

    cursor.close()
    db_con.close()
    return rows

def run_airport_distance():
  first_airport = input("Enter the ICAO code of the first airport: ").upper().strip()
  second_airport = input("Enter the ICAO code of the second airport: ").upper().strip()
  first_coords = get_airport_coordinates(first_airport)
  second_coords = get_airport_coordinates(second_airport)

  if not first_coords:
      print(f"Airport with ICAO code {first_airport} not found in the database.")
      return
  if not second_coords:
      print(f"Airport with ICAO code {second_airport} not found in the database.")
      return

  distance = geodesic(first_coords, second_coords).kilometers
  print("")
  print("")
  print(f"Distance between {first_airport} and {second_airport}: {distance:.2f} kilometers")

run_airport_distance()
