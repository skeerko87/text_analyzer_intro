'''
author = Bohuslav Dvořák
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

SEZNAM_UZIV = ("bob", "ann", "mike", "liz")
SEZNAM_HESEL = ("123", "pass123", "password123")
ODDELOVAC = "-" * 40

print(ODDELOVAC)
print("Vítejte v aplikaci. Prosím přihlaste se: ")

uzivatel = input("USERNAME: ")
if not uzivatel in SEZNAM_UZIV:
    print("Toto jméno není registrováno!")
    exit()

heslo = input("PASSWORD: ")
if not heslo in SEZNAM_HESEL:
    print("Toto heslo není registrováno!")
    exit()

print(ODDELOVAC)

print(f"Máme {len(TEXTS)} druhy textů k analýze.")
text_uzivatel = int(input("Vyberte druh textu od 1 do 3: "))

text_vyber = TEXTS[text_uzivatel-1]

print(ODDELOVAC)

print(f"Zvolený druh textu obsahuje {len(text_vyber.split())} slov.")

clean_words = [w.strip(',.') for w in text_vyber.split()]

zacatek_velky = 0
male = 0
velke = 0
cisla = 0
pocitadlo = {}
soucet = 0

x = 0
while x < len(clean_words):
    if clean_words[x].istitle():
        zacatek_velky = zacatek_velky + 1
    elif clean_words[x].isupper():
        velke = velke + 1
    elif clean_words[x].islower():
        male = male + 1
    elif clean_words[x].isnumeric():
        cisla = cisla + 1
        soucet = soucet + int(clean_words[x])

    y = len(clean_words[x])
    pocitadlo[y] = pocitadlo.get(y,0) + 1
    x = x + 1

print(f"Zvolený druh textu obsahuje {zacatek_velky} slov začínajících velkými písmeny.")
print(f"Zvolený druh textu obsahuje {velke} slov s velkými písmeny.")
print(f"Zvolený druh textu obsahuje {male} slov s malými písmeny.")
print(f"Zvolený druh textu obsahuje {cisla} číslice.")
print(ODDELOVAC)

pocitadlo_1 = sorted(pocitadlo)

z = 0
while z < len(pocitadlo_1):
    pocitadlo_2 = pocitadlo_1[z]
    vyskyt = pocitadlo[pocitadlo_2]
    if len(str(pocitadlo_2)) == 1:
        delka_sl = ' ' + str(pocitadlo_2)
    else:
        delka_sl = str(pocitadlo_2)
    print(delka_sl, '*' * vyskyt, vyskyt)
    z = z + 1

print(ODDELOVAC)
print(f"Součet všech čísel ve zvoleném textu je: {str(soucet)}")
print(ODDELOVAC)