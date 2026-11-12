# Bonus 3 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Kámen, nůžky, papír. Zeptej se obou hráčů na tah – ať zadají
#     "kamen", "nuzky" nebo "papir". Vypiš, kdo vyhrál:
#       - "Remíza.", když mají oba stejně,
#       - jinak urči vítěze podle pravidel:
#           kámen tupí nůžky, nůžky stříhají papír, papír balí kámen.
#     Vypiš "Vyhrál hráč 1." / "Vyhrál hráč 2.".

hrac_1 = input("Hráč 1 (kamen/nuzky/papir): ")
hrac_2 = input("Hráč 2 (kamen/nuzky/papir): ")
if hrac_1 == hrac_2:
    print("Remíza.")
elif (hrac_1 == "kamen" and hrac_2 == "nuzky") or (hrac_1 == "nuzky" and hrac_2 == "papir") or (hrac_1 == "papir" and hrac_2 == "kamen"):
    print("Vyhrál hráč 1.")
else:
    print("Vyhrál hráč 2.")