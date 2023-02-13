## Functions

def combinaison(liste):
    combinaisons = []  
    for a in liste:
        for b in liste:
            for c in liste:
                if a != b != c and a < b <c:
                    abc = f"{a}{b}{c}"
                    combinaisons.append(abc)
    return combinaisons

def affichage(liste):
    result = ""
    for i in liste:
        result += f"{i}, "
    return result


## Parsing

liste_chiffres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


## Resolution

resultat = combinaison(liste_chiffres)


## Display

display = affichage(resultat)

print(display)
