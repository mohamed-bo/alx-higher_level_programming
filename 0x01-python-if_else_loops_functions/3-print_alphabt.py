#!/usr/bin/python3
for letter in range(97, 123):
    if letter is not (ord('q')) and letter is not (ord('e')):
        print('{}'.format(chr(letter)), end='')
