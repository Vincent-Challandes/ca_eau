## Modules and Functions
import sys

def nb_premier(a):
    if a > 2:
        while True:
            # on créer une boucle ou l'on cherche a savoir si on peut diviser notre nombre par autre choses que lui-même et et 1 
            for i in range(2, a):
                reste = a % i
                if reste == 0:
                    break
            if reste != 0:
                return a
            else:
                a += 1
    else:
        return 2
                  

## Error handling

if len(sys.argv) != 2:
    print("-1")
    sys.exit()

if not sys.argv[1].isdigit():
    print("-1")
    sys.exit()


## Parsing

nombre = int(sys.argv[1])


## Resolution 

resultat = nb_premier(nombre)


## Display

print(resultat)
