## Functions

def liste_0_à_9():
    liste = []
    for i in range(10):
        liste.append(i)
    return liste

def combinaison(liste):
    combinaisons = []  
    for a in liste:
        for b in liste:
            for c in liste:
                if a < b < c:
                    abc = f"{a}{b}{c}"
                    combinaisons.append(abc)
    return combinaisons

def affichage(liste):
    result = ""
    for i in liste:
        result += f"{i}, "
    return result


## Parsing

liste_chiffres = liste_0_à_9()


## Resolution

resultat = combinaison(liste_chiffres)


## Display

display = affichage(resultat)

print(display)
