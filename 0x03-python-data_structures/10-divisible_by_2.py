#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boo_list = []
    for i in my_list:
        if i % 2 == 0:
            boo_list.append(True)
        else:
            boo_list.append(False)
    return boo_list
