# Cvičení 5 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na počet bodů z testu (0 až 100) a vypiš známku:
#    90 a víc → 1, 75 a víc → 2, 60 a víc → 3, 40 a víc → 4,
#    jinak → 5.

pocet_bodu = int(input("Jaký mas pocet bodu z testu ?"))
if pocet_bodu >= 90:
    print("Mas znamku 1")
elif pocet_bodu >= 75:
    print("Mas znamku 2")
elif pocet_bodu >= 60:
    print("Mas znamku 3")
elif pocet_bodu >= 40:
    print("Mas znamku 4")
else:
    print("Mas znamku 5")


