#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for i, num in enumerate(r):
            print("{:d}".format(num), end="")
            if i < len(r) - 1:
                print(" ", end="")
        print("")
