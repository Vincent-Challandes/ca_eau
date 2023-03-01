## Module and Functions and Variables globals

import sys

def check_count_argv(arguments):
    if not len(arguments) == 2:
        print("error !")
        sys.exit()

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

check_count_argv(sys.argv)

is_alphabet(sys.argv[1])


## Parsing

string = sys.argv[1]


## Resolution

resultat = majuscule(string)


## Display

print(resultat)

print("hello")
