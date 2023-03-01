# Function 

import sys

def check_nb_argv(liste):
    if len(liste) == 1:
     print("erreur : veuillez entrer un ou des arguments")
     sys.exit()

def afficheur_arguments(liste):
    # la on parcour notre tableau de la fin au début
    for i in liste[::-1]:
        if i == arguments[0]:
            continue
        else:
            # on print direct afin de pas avoir a stocker un nouveau tableau inversé
            print(i)
            

## Error handling

check_nb_argv(sys.argv)


## Parsing

arguments = sys.argv


# Resolution

afficheur_arguments(arguments)
