class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.cislo = cislo

    def to_string(self):
        return f"{self.jmeno}, {self.prijmeni}, {self.vek}, {self.cislo}"
