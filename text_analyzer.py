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

zacatek_velky = 0
velke = 0
male = 0
cisla = 0
soucet_cisel = 0

for x in text_vyber:
    if (x.istitle()) == True:
        zacatek_velky+= 1
    elif (x.isupper()) == True:
        velke+= 1
    elif (x.islower()) == True:
        male+= 1
    elif (x.isnumeric()) == True:
        cisla+= 1

print(f"Zvolený druh textu obsahuje {zacatek_velky} slov začínajících velkými písmeny.")
print(f"Zvolený druh textu obsahuje {velke} slov s velkými písmeny.")
print(f"Zvolený druh textu obsahuje {male} slov s malými písmeny.")
print(f"Zvolený druh textu obsahuje {cisla} číslice.")
print(ODDELOVAC)

clean_words = [w.strip(',.') for w in text_vyber.split()]

num = [num for num, word in enumerate(clean_words)]

for num,word in enumerate(clean_words):
    print(num, "*".format(word) * len(word), len(word))

print(ODDELOVAC)
print(f"Součet všech čísel ve zvoleném textu je:") # Tohle fakt nevím :-)
print(ODDELOVAC)