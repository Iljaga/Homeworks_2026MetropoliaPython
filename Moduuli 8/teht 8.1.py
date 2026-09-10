import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="YOUR_PASSWORD",
    autocommit=True
)

icao = input("Anna lentoaseman ICAO-koodi: ").upper()

cursor = connection.cursor()

sql = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(sql, (icao,))

result = cursor.fetchone()

if result:
    print(f"Lentoasema: {result[0]}")
    print(f"Sijaintikunta: {result[1]}")
else:
    print("Lentoasemaa ei löytynyt.")

cursor.close()
connection.close()