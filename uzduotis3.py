# Duotas sąrašas: sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# 1.1. Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą

sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
kitas_sarasas = []
sudetas_sarasas = sum([x for x in sarasas if type(x) in [float, int]])
print(f" 1.1. Skaičių suma: {sudetas_sarasas}")

# 1.2. Sudėtų ir atspausdintų visus sąrašo žodžius.
sudek_zodzius = [x for x in sarasas if type(x) is str]
print(f' 1.2. {" ".join(sudek_zodzius)}')

# 1.3. Suskaičiuotų ir atspausdintų,kiek  yra loginių (boolean) kintamųjų su True reikšme.
kiek_loginiu = sum([type(x) is bool for x in sarasas])
print(f" 1.3. 'True' reikšmių kiekis: {kiek_loginiu}")
# su filter:
#kiekis_loginiu = sum(filter(lambda x: type(x) is bool, sarasas))
#print(kiekis_loginiu)