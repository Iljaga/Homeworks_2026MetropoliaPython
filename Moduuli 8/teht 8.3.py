import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="YOUR_PASSWORD",
    autocommit=True
)

icao1 = input("Anna ensimmäisen lentoaseman ICAO-koodi: ").upper()
icao2 = input("Anna toisen lentoaseman ICAO-koodi: ").upper()

cursor = connection.cursor()

sql = """
SELECT latitude_deg, longitude_deg
FROM airport
WHERE ident = %s
"""

cursor.execute(sql, (icao1,))
airport1 = cursor.fetchone()

cursor.execute(sql, (icao2,))
airport2 = cursor.fetchone()

if airport1 and airport2:
    distance = geodesic(airport1, airport2).kilometers
    print(f"Lentoasemien välinen etäisyys on {distance:.2f} km.")
else:
    print("Toista tai molempia lentoasemia ei löytynyt.")

cursor.close()
connection.close()