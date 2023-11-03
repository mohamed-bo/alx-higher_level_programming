#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_v = my_list[0]
    for n in my_list[1:]:
        if n > max_v:
            max_v = n
    return max_v
