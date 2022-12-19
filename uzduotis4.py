# Naudoti sorted, attrgetter, reverse, funkciją repr
# from operator import attrgetter


# 4.1. Turėtų klasę Zmogus, su savybėmis vardas ir amzius.
# 4.2. Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return f" Zmogus(name = {self.vardas}, amzius = {self.amzius})" #negerai cia kazkas

# 4.3. Inicijuoti kelis Zmogus objektus su vardais ir amžiais.

asmuo = Zmogus("Juozas", 64)
asmuo1 = Zmogus("Vincas", 73)
asmuo2 = Zmogus("Paulius", 13)
asmuo3 = Zmogus("Aurora", 19)
asmuo4 = Zmogus("Vincentas", 3)

# 4.4. Įdėti sukurtus Zmogus objektus į naują sąrašą.
zmogai = [asmuo, asmuo1, asmuo2, asmuo3, asmuo4]

# 4.5.  Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)