## Functions

def creer_liste_nombre(liste):
    liste_nb = []
    for a in liste:
        for b in liste:
            nb = f"{a}{b}"
            liste_nb.append(nb)
    return liste_nb

def combinaison(liste):
    liste_combinaisons = []
    for a in liste:
        for b in liste:
            if a < b:
                ab = f"{a} {b}"
                liste_combinaisons.append(ab)
    return liste_combinaisons

def affichage(liste):
    result = ""
    for i in liste:
        result += f"{i}, "
    return result


## Parsing

liste_chiffre = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

liste_nombre = creer_liste_nombre(liste_chiffre)


## Resolution 

resultat = combinaison(liste_nombre)


## Display

display = affichage(resultat)

print(display)
