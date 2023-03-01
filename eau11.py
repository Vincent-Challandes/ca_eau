## Modules and Functions

import sys

def check_nb_args(args):
    if len(args) < 3:
        print("error !")
        sys.exit()

# fonction check si nombre positif/négatif
def chiffre_only(liste):
    for c in liste:
        if not c.lstrip("-").isdigit():
            print("error format !")
            sys.exit()

# fonction triage            
def triage(nombres, nombre_nombre):
    # on créer une première boucle avec un nombre de passage égale au nombre d'argument dans notre liste nombres
    # on fait ca car on doit passer la fonction de trie autant de fois qu'il y a d'argument afin d'être sur d'avoir passer tous les nombre avec chaque nombre
    for j in range(nombre_nombre):
             
        # puis on va créer un seconde boucle ou on va trié la liste
        # range(0, nombre_nombre - j -1) permet de partir du début de la liste et de finir à chaque tour 1 argument en moins (j) et le -1 c'est pour pas avoir l'erreur de compérer le dernier chiffre avec un arguements inexistant
        # on fait ça car à chaque tour on prend le plus grand nombre et on le met à la fin donc plus on avance plus la fin est dejà trié
        for i in range(0, nombre_nombre - j -1):
                 
            # ici la structure conditionnel va trié la liste
            # par-contre le cas ou deux nombre sont égaux on retourne un erreur
            # !!! ATTENTION il faut convertir en integer sinon ne trie pas completement la liste
            nombres[i] = int(nombres[i])
            nombres[i + 1] = int(nombres[i + 1])
            if nombres[i] == nombres[i + 1]:
                print("erreur deux fois le même nombre ! ")
                sys.exit()
                 
            elif nombres[i] > nombres[i + 1]:
                nombres[i], nombres[i + 1] = nombres[i + 1], nombres[i]
    
    return nombres

# fonction trouver diff min
def mini_abs(liste):

    # la on gère l'initialisation de la variable result de facon à être plus grande que toute différence possible 
    if int(liste[0] < 0):
        result = int(liste[-1]) - int(liste[0]) 
    else: 
        result = int(liste[-1])
        
    # ici -1 dans la fonction range pour pas finir out of the range à cause du i + 1
    for i in range(len(liste) - 1):
        diff = int(liste[i + 1]) - int(liste[i])
        if diff < result:
            result = diff
    return result


## Error handling

check_nb_args(sys.argv)

chiffre_only(sys.argv[1:])


## Parsing

liste_nombres = sys.argv[1:]


## Resolution

liste_triee = triage(liste_nombres, len(liste_nombres))

resultat = mini_abs(liste_triee)


## Display

print(resultat)
