import flask
import mysql.connector

app = flask.Flask(__name__)
db_con = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='password',
         autocommit=True
         )

def get_airport_by_icao(icao: str) -> dict:
    cursor = db_con.cursor(dictionary=True)
    try:
        cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao,))
        return cursor.fetchone()
    finally:
        cursor.close()

@app.get("/airport/<string:icao>")
def get_airport_by_icao_handler(icao: str):
    airport = get_airport_by_icao(icao)

    if airport is None:
        return {"ICAO": "", "Name": "", "Municipality":""}, 404

    return {"ICAO": icao, "Name": airport["name"], "Municipality": airport["municipality"]}
if __name__ == "__main__":
    app.run("0.0.0.0", 3000)
