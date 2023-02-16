## Modules and Functions

import sys

def chiffre_only(liste):
    for c in liste:
        if not c.lstrip("-").isdigit():
            print("error format !")
            sys.exit()

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        # Flag permettant de voir si tableau déjà trié
        trier = True
        # Parcour le array
        for j in range(0, n - i - 1):
            # Si élément courant plus grand que le suivant on les échange
            # ATTENTION convert in int! sinon tri pas correctement la liste
            array[j], array[j + 1] = int(array[j]), int(array[j + 1])
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                trier = False
        # Si array trié on sort de la boucle
        if trier:
            break
    return array

def affichage(array):
    result = ""
    for i in array:
        result += f"{i} "
    print(result)


## Error handling

if len(sys.argv) < 3:
    print("error !")
    sys.exit()

chiffre_only(sys.argv[1:])


## Parsing

array = sys.argv[1:]


## Resolution

new_array = bubble_sort(array)


## Display

affichage(new_array)
