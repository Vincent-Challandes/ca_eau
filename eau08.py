## Module and Functions and Variables globals

import sys
import re

def error_handling(arguments):
    if not len(arguments) == 2:
        print("error !")
        sys.exit()


def chiffres_only(string):
    result = ""
    for i in range(len(string)):
        # utilisation de regex pour ne pas avoir a écrir un array avec tous les chiffre
        if re.search("[^0-9]", string[i]):
            result = "false"
            break
        else:
            result = "true"
    return result
        

## Error handling

error_handling(sys.argv)


## Parsing

string = sys.argv[1]


## Resolution

resultat = chiffres_only(string)


## Display

print(resultat)
