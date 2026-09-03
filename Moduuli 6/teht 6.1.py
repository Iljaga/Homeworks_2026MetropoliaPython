import random

def heita_noppaa():
    return random.randint(1, 6)

while True:
    silmaluku = heita_noppaa()
    print(silmaluku)

    if silmaluku == 6:
        break