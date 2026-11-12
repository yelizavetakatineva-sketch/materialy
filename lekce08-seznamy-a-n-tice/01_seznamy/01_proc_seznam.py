# ---------------------------------------------
#  Proč seznam
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

# Pořádáš večírek a chceš si zapsat hosty. Zatím umíš tohle:
host1 = "Anna"
host2 = "Petra"
host3 = "Jana"

# Stejně sis v lekci 2 psala známky: znamka1, znamka2, znamka3. Co když
# přijde dalších dvacet lidí? Na každého bys potřebovala novou proměnnou
# a cyklem bys je neprošla.


# Seznam drží víc hodnot v jedné proměnné. Píše se do hranatých závorek
# a hodnoty oddělují čárky:
hoste = ["Anna", "Petra", "Jana"]

print(hoste)            # ['Anna', 'Petra', 'Jana']
print(len(hoste))       # 3 – počet položek v seznamu

print ("-"* 30)
print ("Pomoci for")

for host in hoste:
    print("Zvu Vas na Vanocni vecirek", host)

print ("Prvni byla pozvana" , hoste[0])

print ("-"* 30)
print ("Pomoci range")

for i in range(pocethostu):
    print("Zvu Vas na Vanocni vecirek", hoste[i])

blacklist = ["Hegerova", "vlk"]

prichozi = input("Jak se jmenujes?")

for host in hoste:
    if prichozi == host:
        print("Pod dal:", prichozi)  
        
# Hodnoty stojí v pořadí, v jakém jsi je napsala, a můžou se opakovat.
# Vejdou se do něj i čísla:
hlasy = [1, 2, 1, 1]

print(hlasy)            # [1, 2, 1, 1]


# Do seznamu dáš jakékoli hodnoty: text, celá i desetinná čísla, True
# a False, a dokonce i další seznam:
ruzne = ["Anna", 34, 1.5, True, ["dort", "víno"]]

print(ruzne)            # ['Anna', 34, 1.5, True, ['dort', 'víno']]
print(len(ruzne))       # 5 – vnitřní seznam je jedna položka

# Míchat různé druhy hodnot v jednom seznamu ale nebývá dobrý nápad.
# V cyklu bys u každé položky musela hlídat, co je zač. Obvykle má
# seznam hodnoty jednoho druhu: samá jména, samá čísla.


# Seznam může být i prázdný. Hodí se to, když hodnoty teprve přibudou:
omluveni = []

print(omluveni)         # []
print(len(omluveni))    # 0
