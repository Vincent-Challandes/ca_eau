## Modules and Fonction 

import sys

def error_handling(arguments):
    if len(arguments) != 3:
        print("error !")
        sys.exit()

    if arguments[1].isdigit() or arguments[2].isdigit():
        print("error !")
        sys.exit()

def string_string(st1, st2):
    # range(on enlève la longueur de la substring pour pas avoir à itérer toute la main_string
    # et ajoute 1 sinon on contrôle pas la dernière lettre possible dans la main_string)
    for i in range(len(st1) - len(st2) + 1):
        if st2 == st1[i:i + len(st2)]:
            return True   
    return False


## Error handling

error_handling(sys.argv)


## Parsing

st1 = sys.argv[1]

st2 = sys.argv[2]


## Resolution 

resultat = string_string(st1, st2)


## Display

print(resultat)
