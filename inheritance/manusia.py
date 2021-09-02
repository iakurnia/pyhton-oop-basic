from inheritance.makhluk_hidup import MakhlukHidup


class Manusia(MakhlukHidup):
    def __init__(self, ciri_khas):
        self.ciri_khas = ciri_khas

    def info(self):
        return 'Ini Class Manusia'

    def data(self):
        return f'Ciri Khas nya adalah {self.ciri_khas}'
