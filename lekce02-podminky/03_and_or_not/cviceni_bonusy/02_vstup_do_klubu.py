# Bonus 2 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Vstup do klubu. Dovnitř smí ten, komu je aspoň 18 let A ZÁROVEŇ
#     je buď členem, NEBO má pozvánku.
#     Kdo má zákaz vstupu, dovnitř nesmí nikdy – ani člen, ani s pozvánkou.
#     Zamysli se, kam patří závorky, aby podmínka fungovala správně.
#     Vypiš "Vítej v klubu." / "Dnes se nedostaneš.".

vek = int(input("Zadej vek: "))
clenstvi = input("Mas clenstvi? (ano/ne)")
pozvanka = input("Mas pozvanku? (ano/ne")
if vek >= 18 and clenstvi == "ano" or pozvanka == "ano":
    print("Vitej v klubu")
else:
    print("Dnes se nedostaneš.") 