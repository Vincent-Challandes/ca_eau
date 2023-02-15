## Module and Functions and Variables globals

import sys

def is_alphabet(string):
    for c in range(len(string)):
        if string[c].isdigit():
            print("error format!")
            sys.exit()

def majuscule(string):
    result = ""
    for c in range(len(string)):
        if c == 0 or string[c - 1] in [" ", "\n", "\t"]:
            result += string[c].upper()
        else:
            result += string[c].lower()
    return result


## Error handling

if not len(sys.argv) == 2:
    print("error !")
    sys.exit()

is_alphabet(sys.argv[1])


## Parsing

string = sys.argv[1]


## Resolution

resultat = majuscule(string)


## Display

print(resultat)
