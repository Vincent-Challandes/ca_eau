## Modules and Functions

import sys

def error_handling(args):
    if len(args) <= 2:
        print("error!")
        sys.exit()

def index_wanted(array, element):
    for i in range(len(array)):
        if element == array[i]:
            return i
    return -1


## Error handling

error_handling(sys.argv)


## Parsing

array = sys.argv[1:-1]

element = sys.argv[-1]


## Resolution 

resultat = index_wanted(array, element)


## Display

print(resultat)
