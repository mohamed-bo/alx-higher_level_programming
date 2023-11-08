#!/usr/bin/python3
def uniq_add(my_list=[]):
    setL = set(my_list)
    sum = 0
    for i in setL:
        sum += i
    return sum
