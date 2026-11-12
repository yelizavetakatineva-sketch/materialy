# Bonus 2 – Vstup od uživatelky
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na částku a na počet lidí.
#     Vypiš, kolik zaplatí každý a kolik korun zbyde.

castka = int(input("Jaká je castka?"))
lidi = int(input("Jaký je počet lidi?"))
print("Každý zaplatí", castka // lidi)
print("Zbyde", castka % lidi)
            