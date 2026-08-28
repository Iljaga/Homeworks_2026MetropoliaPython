while True:
    tuumat = float(input("Anna tuumamäärä: "))

    if tuumat < 0:
        break

    senttimetrit = tuumat * 2.54
    print(f"{senttimetrit} cm")