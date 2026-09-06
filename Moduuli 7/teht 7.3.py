lentoasemat = {}

while True:
    toiminto = input("Haluatko syöttää uuden lentoaseman, hakea lentoaseman vai lopettaa? (uusi/haku/lopeta): ")

    if toiminto == "uusi":
        icao = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif toiminto == "haku":
        icao = input("Anna lentoaseman ICAO-koodi: ")

        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")

    elif toiminto == "lopeta":
        break