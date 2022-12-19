# Naudoti map, filter arba comprehension,
# sum, min, max, mean, median, %

from statistics import mean, median

# 1.1. Sukurtų sąrašą iš skaičių nuo 0 iki 50

#sk = range(0,51)
#print(list(sk))

# 1.2. Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų.
# su map

#sudauginti_sk = map(lambda x: x * 10, sk)
#print(list(sudauginti_sk))

# 1.2. Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų.
# su list comprehension

#sk = list(range(51))
#sudauginti_sk = [x*10 for x in sk ] # butinai lauztiniai, nes kitaip bus generator
#print(sudauginti_sk)

# 1.3. Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdinstu

#sk = list(range(51))
#sk_su_septyniais = (x for x in sk if x % 7 == 0)
#print(list(sk_su_septyniais)) # reikia list, be jo bus tik generator, o ne masyvas

# 1.4. Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų.
# Šį sąrašą (list masyvą) priskirti naujam kintamajam.

# su map funkcija
paprasti_sk = range(51)
#pakelta_kvadratu = map(lambda x: x**2, paprasti_sk)
#print(list(pakelta_kvadratu))

# 1.5. Su kvadratų sąrašu (nauju kintamuoju) atliktų šiuos veiksmus:
#  atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą.

pakelta_kvadratu = list(map(lambda x: x**2, paprasti_sk)) # butina idet map i list, nes kitu atveju gaunu empty.
print(f" Skaičių kvadratai: {list(pakelta_kvadratu)}")

print(f" Kvadratų suma: {sum(pakelta_kvadratu)}")
print(f" Mažiausias skaičius: {min(pakelta_kvadratu)}")
print(f" Didžiausias skaičius: {max(pakelta_kvadratu)}")
print(f" Vidurkis: {mean(pakelta_kvadratu)}")
print(f" Mediana: {median(pakelta_kvadratu)}")

# 1.6. Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
mazejanciai = sorted(pakelta_kvadratu, reverse=True)
print(f"\n Mažėjimo tvarka: {mazejanciai}")