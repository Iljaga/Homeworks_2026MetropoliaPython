vuosi = int(input("Anna vuosiluku: "))

# Jos vuosi on jaollinen 400:lla, se on karkausvuosi
if vuosi % 400 == 0:
    print("Vuosi on karkausvuosi.")

# Jos vuosi on jaollinen 100:lla, mutta ei 400:lla,
# se ei ole karkausvuosi
elif vuosi % 100 == 0:
    print("Vuosi ei ole karkausvuosi.")

# Jos vuosi on jaollinen 4:llä, se on karkausvuosi
elif vuosi % 4 == 0:
    print("Vuosi on karkausvuosi.")

# Muut vuodet eivät ole karkausvuosia
else:
    print("Vuosi ei ole karkausvuosi.")