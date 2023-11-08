#!/usr/bin/python3
def roman_to_int(roman_string):
    n = 0
    if roman_string is None or type(roman_string) is not str:
        return 0
    trDict = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n += trDict[roman_string[0]]
    for i in range(1, len(roman_string)):
        if trDict[roman_string[i]] > trDict[roman_string[i - 1]]:
            n += trDict[roman_string[i]] - 2 * trDict[roman_string[i - 1]]
        else:
            n += trDict[roman_string[i]]
    return n
