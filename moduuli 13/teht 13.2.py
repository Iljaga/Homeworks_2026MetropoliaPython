
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/kentta/<icao>', methods=['GET'])
def get_airport(icao):

    connection = sqlite3.connect('airports.db')
    cursor = connection.cursor()

    cursor.execute(
        "SELECT ident, name, municipality FROM airport WHERE ident = ?",
        (icao.upper(),)
    )

    result = cursor.fetchone()
    connection.close()

    if result:
        airport = {
            "ICAO": result[0],
            "Name": result[1],
            "Municipality": result[2]
        }
        return jsonify(airport)

    return jsonify({"error": "Lentokenttää ei löytynyt"}), 404


if __name__ == '__main__':
    app.run(port=3000)
