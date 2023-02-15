## Modules and Functions

import sys

# fonction pour définir min max
def which_min_max(a, b):
    if a == b:
        print("error min = max!")
        sys.exit()
    elif a < b:
        min = a
        max = b
    else:
        min = b
        max = a
    return min, max

# fonction créer liste de nombre 
def min_max(min, max):
    liste = []
    i = min
    while i < max:
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

# check nb arguments
if len(sys.argv) != 3:
    print("error !")
    sys.exit()

# check format argument
if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("error format!")
    sys.exit()


## Parsing 

nb1, nb2 = int(sys.argv[1]), int(sys.argv[2])


## Resolution

min, max = which_min_max(nb1, nb2)

liste_nb = min_max(min, max)


## Display

print_liste(liste_nb)
