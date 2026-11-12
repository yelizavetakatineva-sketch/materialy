# Cvičení 4 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Máš proměnnou barva se stavem semaforu ("červená", "oranžová"
#    nebo "zelená"). Vypiš, co má řidič udělat:
#    "červená" → "Stůj", "oranžová" → "Připrav se", "zelená" → "Jeď",
#    cokoli jiného → "Neznámý signál".
barva = "zelená"

if barva == "červená": 
   print("Stuj")
elif barva == "oranžová":
    print("Připrav se!")
elif barva == "zelená":
    print("Jed!")
else:
    print("Chyba semaforu")