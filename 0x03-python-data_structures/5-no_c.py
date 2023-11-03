#!/usr/bin/python3
def no_c(my_string):
    result = []
    for letter in my_string:
        if letter not in 'cC':
            result.append(letter)
    return ''.join(result)
