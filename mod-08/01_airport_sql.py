import mysql.connector


db_con = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='password',
         autocommit=True
         )


def get_airport_by_icao(icao_code):
    query = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor = db_con.cursor(dictionary=True)
    try:
        cursor.execute(query, (icao_code,))
        return cursor.fetchone()
    finally:
        cursor.close()

ecao_input = input("Enter the ICAO code of an airport: ").upper().strip()


rows = get_airport_by_icao(ecao_input)

if not rows:
    print(f"No airport found with ICAO code {ecao_input}", end='')
else:
    print(f"Airport name: {rows['name']}\nLocation: {rows['municipality']}", end="")
