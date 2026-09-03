import random

luku = int(input("Kuinka monta kuutiota heitetään? "))

summa = 0

for i in range(luku):
    silmaluku = random.randint(1, 6)
    summa += silmaluku

print("Silmälukujen summa on:", summa)