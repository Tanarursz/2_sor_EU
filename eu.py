bananido = open("EUcsatlakozas.txt", "r")

tomb=[]
for sor in bananido:
    tomb.append(sor.strip().split(";"))
    
bananido.close()

# 3.
print(f"3. feladat: EU tagállamainak száma: {len(tomb)} db")

# 4. 2007-ben
szamlalo = 0 
for sor in tomb:
    if (sor[1][0:4]) == "2007":
        szamlalo = szamlalo +1
        
print(f"4. feladat: 2007-ben {szamlalo} ország csatlakozott.")

# 5. Magyarország dátum

for sor in tomb:
    if (sor[0]) == "Magyarország":
        magyarorszag = sor
        
print(f"5. feladat: Magyarország {sor[1]} ország csatlakozott.")

