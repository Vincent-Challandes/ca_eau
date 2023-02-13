# Function 

import sys
def afficheur_arguments(a):
    result =[]
    for i in a:
        if i == arguments[0]:
            continue
        else:
            result.append(i)
    return result[::-1]

def print_list(a):
    for element in a:
        print(element)

## Error handling

if len(sys.argv) == 1:
     print("erreur : veuillez entrer un ou des arguments")
     sys.exit()

## Parsing

arguments = sys.argv


# Resolution

resultat = afficheur_arguments(arguments)


# Display

print_list(resultat)
