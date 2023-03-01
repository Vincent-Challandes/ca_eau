## Modules and Functions
import sys

def error_handling(arguments):
    if len(arguments) != 2:
        print("-1")
        sys.exit()

    if not arguments[1].isdigit():
        print("-1")
        sys.exit()

def nb_premier(nb):
    if nb > 2:
        while True:
            # on créer une boucle ou l'on cherche a savoir si on peut diviser notre nombre par autre choses que lui-même et et 1 
            for i in range(2, nb):
                reste = nb % i
                if reste == 0:
                    break
            if reste != 0:
                return nb
            else:
                nb += 1
    else:
        return 2
                  

## Error handling

error_handling(sys.argv)


## Parsing

nombre = int(sys.argv[1])


## Resolution 

resultat = nb_premier(nombre)


## Display

print(resultat)
