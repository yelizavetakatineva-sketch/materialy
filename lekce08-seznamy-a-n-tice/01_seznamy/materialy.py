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
        
def kontrola(prichozi):
    if prichozi in hoste:
        print("pojd dal,", prichozi)
    elif prichozi in blacklist:
        print("zmiz dal,", prichozi)
    else:
        print("Nejsi zvan")

# kontrola(prichozi, hoste, blacklist)

def pozvi(jmeno, hoste):
    hoste.append(jmeno)

pozvi("Vojta", hoste)
print(hoste)
hoste [5:5] = ["Tom"]
print (hoste)