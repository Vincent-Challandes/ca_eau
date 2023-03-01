## Modules and Functions

import sys

def error_handling(args):
    # check nb arguments
    if len(args) != 3:
        print("error !")
        sys.exit()

    # check format argument
    if not args[1].isdigit() or not args[2].isdigit():
        print("error format!")
        sys.exit()

# fonction pour définir min max
def which_min_max(nb1, nb2):
    if nb1 == nb2:
        print("error min = max!")
        sys.exit()
    elif nb1 < nb2:
        min = nb1
        max = nb2
    else:
        min = nb2
        max = nb1
    return min, max

# fonction créer liste de nombre 
def min_max(nb_min, nb_max):
    liste = []
    i = nb_min
    while i < nb_max:
        liste.append(i)
        i += 1
    return liste

# fonction pour print une liste
def print_liste(liste):
    result = ""
    for i in liste:
        result += f"{i} "
    print(result)


## Error handling

error_handling(sys.argv)


## Parsing 

nb1, nb2 = int(sys.argv[1]), int(sys.argv[2])


## Resolution

nb_min, nb_max = which_min_max(nb1, nb2)

liste_nb = min_max(nb_min, nb_max)


## Display

print_liste(liste_nb)
