## Modules and Functions

import sys

def check_nb_args(args):
    if len(args) < 3:
        print("error !")
        sys.exit()

def selection_sort(array):
    n = len(array)
    # permet de parcourir tous le tableau
    for i in range(n - 1):
        # index_min permet de prendre l'élément minimum du tableau
        index_min = i
        for j in range(i + 1, n):
            # sans convertion les éléments d'un tableau sont type str et donc trié par ordre ASCII
            
            if array[j] < array[index_min]:
                index_min = j
        
        if index_min != i:
            array[i], array[index_min] = array[index_min], array[i]
        
    return array

def affichage(array):
    result = ""
    for i in array:
        result += f"{i} "
    print(result)


## Error handling

check_nb_args(sys.argv)


## Parsing

array = sys.argv[1:]


## Resolution

new_array = selection_sort(array)


## Display

affichage(new_array)
