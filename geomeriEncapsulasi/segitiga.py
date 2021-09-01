class Segitiga():
    def __init__(self, a, t):
        # fungsi yang d baca pertama jika object di ciptakan (Construktor)
        self.a = a
        self.t = t

    def info(self):
        return f'Geomeri Segitiga (L=a*t/2) dari Alas : {self.a} dan Tinggi : {self.t}'

    def luas(self):
        luas = self.a * self.t / 2
        return luas
