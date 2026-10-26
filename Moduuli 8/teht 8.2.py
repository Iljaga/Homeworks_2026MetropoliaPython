import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="YOUR_PASSWORD",
    autocommit=True
)

country = input("Anna maakoodi: ").upper()

cursor = connection.cursor()

sql = """
SELECT type, COUNT(*)
FROM airport
WHERE iso_country = %s
GROUP BY type
ORDER BY type
"""

cursor.execute(sql, (country,))

results = cursor.fetchall()

if results:
    for airport_type, amount in results:
        print(f"{airport_type}: {amount}")
else:
    print("Lentokenttiä ei löytynyt.")

cursor.close()
connection.close()