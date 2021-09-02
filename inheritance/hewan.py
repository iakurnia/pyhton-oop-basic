from inheritance.makhluk_hidup import MakhlukHidup


class Hewan(MakhlukHidup):
    def __init__(self, ciri_khas):
        self.ciri_khas = ciri_khas

    def info(self):
        return 'Ini Class Hewan'

    def data(self):
        return f'Ciri Khas Hewan adalah {self.ciri_khas}'
