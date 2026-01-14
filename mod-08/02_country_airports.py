import mysql.connector

def get_airports_by_country(country_code):
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
        SELECT type, COUNT(*) AS cnt
        FROM airport
        WHERE iso_country = %s
        GROUP BY type
        ORDER BY type
    """
    cursor.execute(query, (country_code,))
    rows = cursor.fetchall()

    cursor.close()
    db_con.close()
    return rows

def run_country_program():
    country = input("Enter the country code (e.g., FI for Finland): ").strip().upper()
    rows = get_airports_by_country(country)

    if not rows:
      print(f"No airports found for country code '{country}' or database connection failed.")
    else:
      print("")
      print("")
      print(f"Airports in {country}:")
      for airport_type, cnt in rows:
          print(f"{cnt} {airport_type} airports")

run_country_program()
