# Prie kiekvieno sakinio "The Zen of Python" žodžio
# pridėtų šauktuką ir atspausdintų naują sakinį.

tekstas = "The Zen of Python"

prideti_sauktukai = map(lambda zenklas: zenklas + "!", tekstas.split()) # isskirstom po zodi

print(" ".join(prideti_sauktukai)) # su join vel sujungiam