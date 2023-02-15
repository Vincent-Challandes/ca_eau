## Module and Functions and Variables globals

import sys

liste_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ! "
liste_min = "abcdefghijklmnopqrstuvwxyz! "

# Convertie une string en minuscule (pourrait avoir en entrée des min et des MAJ, chiffre symbole etc)
def minuscule(lettre):
    result = ""
    for c in range(len(lettre)):
        if lettre[c] in liste_maj:
            for i in range(28):
                if lettre[c] == liste_maj[i]:
                    result += liste_min[i]
        else:
            result += lettre[c]
    return result

# Convertie une string en MAJUSUCULE (pourrait avoir en entrée des min et des MAJ, chiffre symbole etc)
def majuscule(lettre):
    result = ""
    for c in range(len(lettre)):
        if lettre[c] in liste_min:
            for i in range(28):
                if lettre[c] == liste_min[i]:
                    result += liste_maj[i]
        else:
            result += lettre[c]
    return result

def is_alphabet(string):
    for c in range(len(string)):
        if not string[c] in liste_min and not string[c] in liste_maj:
            print("error format!")
            sys.exit()

def majuscule_sur_deux(string):
    # attention de déclarer les variable de mise a zéro avant les boucles sinon remise a zéro à chaque tour
    x = 0
    result = ""  
    for a in range(len(string)):
        if string[a] == " " or string[a] == "!":
            result += string[a]
            continue
        if x % 2 == 0:
            result += majuscule(string[a])
            x += 1
        else:
            result += minuscule(string[a])
            x += 1
    return result


## Error handling

if not len(sys.argv) == 2:
    print("error !")
    sys.exit()

is_alphabet(sys.argv[1])


## Parsing

string = sys.argv[1]


## Resolution

resultat = majuscule_sur_deux(string)


## Display

print(resultat)
