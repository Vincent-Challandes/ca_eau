## Module and Functions and Variables globals

import sys
import re

liste_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
liste_min = "abcdefghijklmnopqrstuvwxyz"

# ma propre fonction lower()
# Convertie une string en minuscule (pourrait avoir en entrée des min et des MAJ, chiffre symbole etc)
def minuscule(lettre):
    result = ""
    for c in range(len(lettre)):
        if lettre[c] in liste_maj:
            for i in range(26):
                if lettre[c] == liste_maj[i]:
                    result += liste_min[i]
        else:
            result += lettre[c]
    return result

# ma propre fonction upper()
# Convertie une string en MAJUSUCULE (pourrait avoir en entrée des min et des MAJ, chiffre symbole etc)
def majuscule(lettre):
    result = ""
    for c in range(len(lettre)):
        if lettre[c] in liste_min:
            for i in range(26):
                if lettre[c] == liste_min[i]:
                    result += liste_maj[i]
        else:
            result += lettre[c]
    return result

def check_count_argv(arguments):
    if not len(arguments) == 2:
        print("error !")
        sys.exit()


def is_digit(string):
        if string.isdigit():
            print("error format!")
            sys.exit()

def majuscule_sur_deux(string):
    # attention de déclarer les variable de mise a zéro avant les boucles sinon remise a zéro à chaque tour
    x = 0
    result = ""  
    for a in range(len(string)):
        # on utilise une regex afin de dire si ce n'est pas une lettre minuscule ou majuscule on garde le caractère telle quel
        # et on continue pour pas incrémenter le conteur x
        if re.search("[^a-zA-Z]", string[a]):
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

check_count_argv(sys.argv)

is_digit(sys.argv[1])


## Parsing

string = sys.argv[1]


## Resolution

resultat = majuscule_sur_deux(string)


## Display

print(resultat)
