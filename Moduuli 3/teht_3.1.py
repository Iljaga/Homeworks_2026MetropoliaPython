pituus = float(input("kuinka paljon cm on kuha?"))

if pituus < 37:
    alamittaisuus = 37 - pituus
    print(f"Kalasi on{alamittaisuus}cm liian lyhyt!")

else:
    print("Voit syödä kalan")