## Module and Functions and Variables globals

import sys

# ma propre fonction isdigit()
def chiffres_only(string):
    liste_chiffre = "0123456789"
    result = ""
    for c in range(len(string)):
        for i in liste_chiffre:
            if i != string[c]:
                result = "false"
            else:
                result = "true"
                break
        if result == "false":
            break
    return result
        

## Error handling

if not len(sys.argv) == 2:
    print("error !")
    sys.exit()


## Parsing

string = sys.argv[1]


## Resolution

resultat = chiffres_only(string)


## Display

print(resultat)
