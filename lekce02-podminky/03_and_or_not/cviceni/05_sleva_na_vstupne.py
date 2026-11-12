# Cvičení 5 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Sleva na vstupné. Slevu mají děti (do 18 let) a senioři (65 a víc).
#    Navíc mají v pondělí slevu úplně všichni.
#    Zeptej se na věk a na den a vypiš "Máš slevu." / "Plné vstupné.".

vek = int(input("Zadej svuj vek: "))
den = input("Zadej den: ")
if vek < 18 and vek >= 65:
    print("Máš slevu.")
elif den == "pondeli":
    print("Máš slevu.")
else:
    print("Plné vstupné.")
