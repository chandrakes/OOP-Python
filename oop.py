class Mobil:
    def __init__(self,roda,tipe,kecepatan):
        self.roda = roda
        self.tipe = tipe
        self.kecepatan = kecepatan
        self.penumpang = 2

    def Melaju(self):
        print('Mobil Melaju ',self.kecepatan)

    def Belok(self,arah):
        print('Belok ',arah)