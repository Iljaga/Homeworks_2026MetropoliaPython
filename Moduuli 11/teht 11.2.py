
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


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


# Pääohjelma
sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

# Asetetaan autojen nopeudet
sahkoauto.kiihdytä(100)
polttomoottoriauto.kiihdytä(120)

# Ajetaan kolme tuntia
sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

# Tulostetaan matkamittarilukemat
print(f"Sähköauton {sahkoauto.rekisteritunnus} matkamittari: "
      f"{sahkoauto.kuljettu_matka} km")

print(f"Polttomoottoriauton {polttomoottoriauto.rekisteritunnus} "
      f"matkamittari: {polttomoottoriauto.kuljettu_matka} km")
