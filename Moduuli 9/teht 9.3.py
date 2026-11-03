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


# Pääohjelma
auto = Auto("ABC-123", 142)

auto.kiihdytä(60)
auto.kulje(1.5)

print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", auto.huippunopeus, "km/h")
print("Tämänhetkinen nopeus:", auto.nopeus, "km/h")
print("Kuljettu matka:", auto.kuljettu_matka, "km")