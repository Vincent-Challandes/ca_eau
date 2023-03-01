## Modules and Functions

import sys

def error_handling(arguments):
    if len(arguments) != 2:
        print("-1")
        sys.exit()

    if not arguments[1].isdigit():
        print("-1")
        sys.exit()

# on va créer une liste de la suite de fibo de la longueur dont on a besoin pour éviter une liste infini
def index_fibo(index):
    suite_fibo = [0, 1]
    for i in range(index + 1):
        if i > 1:
            suite_fibo.append(suite_fibo[i - 1] + suite_fibo[i - 2])
    return suite_fibo[i]


## Error handling

error_handling(sys.argv)


## Parsing

index_recu = int(sys.argv[1])


## Resolution 

resultat = index_fibo(index_recu)


## Display

print(resultat)
