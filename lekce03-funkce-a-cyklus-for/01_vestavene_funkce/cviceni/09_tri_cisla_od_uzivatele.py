# Cvičení 9 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se uživatele na tři čísla (klidně i záporná) a vypiš,
#    jak velké je to největší z nich bez ohledu na znaménko.
#    Např. z čísel -20, 5 a 12 je největší velikost 20.

cislo1 = int(input("Zadej cislo1:"))
cislo2 = int(input("Zadej cislo2:"))
cislo3 = int(input("Zadej cislo3:"))
print(max(abs(cislo1), abs(cislo2), abs(cislo3)))