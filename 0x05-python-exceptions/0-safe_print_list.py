#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for i in range(x):
        try:
            print(my_list[index], end='')
            j += 1
        except Exception as ee:
            break
    print('')
    return j
