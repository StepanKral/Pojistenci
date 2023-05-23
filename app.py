from pojistenec import Pojistenec


class Aplikace:
    def __init__(self):
        self.lide = []

    def vyhledat(self, text):
        vyhledano = []
        for clovek in self.lide:
            if text is None or text.lower() in f"{clovek.jmeno} {clovek.prijmeni}".lower():
                vyhledano.append(clovek)
        return vyhledano

    def pridat(self, jmeno, prijmeni, vek, cislo):
        if len(jmeno) <= 0:
            return False
        if len(prijmeni) <= 0:
            return False
        if not vek.isdigit():
            return False
        if not cislo.isdigit():
            return False
        vek = int(vek)
        if vek < 0:
            return False
        cislo = int(cislo)
        if not (100_000_000 <= cislo < 1_000_000_000):
            return False
        clovek = Pojistenec(jmeno, prijmeni, vek, cislo)
        self.lide.append(clovek)
        return True
