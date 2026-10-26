
import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.nopeus * tuntimäärä


# Luodaan kymmenen autoa
autot = []

for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


# Kilpailu alkaa
while True:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

    # Tarkistetaan, onko joku autoista kulkenut vähintään 10000 km
    if any(auto.kuljettu_matka >= 10000 for auto in autot):
        break


# Tulostetaan tulokset taulukoksi
print(f"{'Rekisteri':<12}{'Huippunopeus':>15}"
      f"{'Nopeus':>12}{'Kuljettu matka':>18}")
print("-" * 57)

for auto in autot:
    print(f"{auto.rekisteritunnus:<12}"
          f"{auto.huippunopeus:>12} km/h"
          f"{auto.nopeus:>9} km/h"
          f"{auto.kuljettu_matka:>14.0f} km")
