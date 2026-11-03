
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi on kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alin_kerros or kohdekerros > self.ylin_kerros:
            print("Virheellinen kerros!")
            return

        while self.kerros < kohdekerros:
            self.kerros_ylös()

        while self.kerros > kohdekerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.hissit = []

        for i in range(hissien_lukumaara):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print("Virheellinen hissin numero!")
            return

        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)


# Pääohjelma
talo = Talo(1, 10, 3)

talo.aja_hissia(1, 5)
talo.aja_hissia(2, 8)
talo.aja_hissia(3, 4)

talo.aja_hissia(1, 1)
talo.aja_hissia(2, 1)
talo.aja_hissia(3, 1)
