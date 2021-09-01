class PersegiPanjang():
    def __init__(self, p, l):
        # fungsi yang d baca pertama jika object di ciptakan (Construktor)
        self.p = p
        self.l = l

    def info(self):
        return f'Geomeri Persegi Panjang (L=p*l) dari Panjang : {self.p} dan Lebar : {self.l}'

    def luas(self):
        luas = self.p * self.l
        return luas
