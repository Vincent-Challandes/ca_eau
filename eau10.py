## Modules and Functions

import sys

def index_wanted(array, element):
    for i in range(len(array)):
        if element == array[i]:
            return i
    return -1


## Error handling

if len(sys.argv) <= 2:
    print("error!")
    sys.exit()


## Parsing

array = sys.argv[1:-1]

element = sys.argv[-1]


## Resolution 

resultat = index_wanted(array, element)


## Display

print(resultat)
