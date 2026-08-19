leiviskät = float(input("Anna leiviskät:\n"))
naulat = float(input("Anna naulat:\n"))
luodit = float(input("Anna luodit:\n"))

# Muutetaan kaikki luodit grammoiksi
luoteina = leiviskät * 20 * 32 + naulat * 32 + luodit

grammat = luoteina * 13.3

kilogrammat = int(grammat // 1000)

grammat = grammat % 1000

print("Massa nykymittojen mukaan:")

print(kilogrammat, "kilogrammaa ja", grammat, "grammaa.")