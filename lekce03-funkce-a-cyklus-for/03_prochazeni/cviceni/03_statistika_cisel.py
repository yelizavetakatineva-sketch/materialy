# Cvičení 3 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Statistika čísel. Uživatel zadá, kolik čísel bude zadávat, a pak
#    ta čísla postupně napíše. V jednom průchodu cyklem spočítej a vypiš
#    jejich součet, průměr, největší a nejmenší číslo.
#    Nepoužívej funkce sum, max ani min – spočítej vše sama cyklem.

pocet = int(input("Kolik cisel zadas?"))

if pocet > 0:
    soucet = 0
    for i in range(pocet):
        cislo = int(input("Zadej číslo: "))
        soucet = soucet + cislo
        if i == 0:
            nejvetsi = cislo
            nejmensi = cislo
    else:
        if cislo > nejvetsi:
            nejvetsi = cislo

        if cislo < nejmensi:
            nejmensi = cislo

    prumer = soucet / pocet
    print("Součet:", soucet)
    print("Průměr:", prumer)
    print("Největší číslo:", nejvetsi)
    print("Nejmenší číslo:", nejmensi)
else:
    print("Musíš zadat alespoň jedno číslo.")