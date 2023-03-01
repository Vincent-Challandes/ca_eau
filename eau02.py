# Function 

import sys

def check_nb_argv(liste):
    if len(liste) == 1:
     print("erreur : veuillez entrer un ou des arguments")
     sys.exit()

def afficheur_arguments(liste):
    result =[]
    for i in liste:
        if i == arguments[0]:
            continue
        else:
            result.append(i)
    return result[::-1]

def print_list(liste):
    for element in liste:
        print(element)

## Error handling

check_nb_argv(sys.argv)


## Parsing

arguments = sys.argv


# Resolution

resultat = afficheur_arguments(arguments)


# Display

print_list(resultat)
