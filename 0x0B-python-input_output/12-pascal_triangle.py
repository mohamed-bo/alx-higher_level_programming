#!/usr/bin/python3
"""
function pascal_triangle
"""


def pascal_triangle(n):
    """
    pascal triangle
    """

    if n <= 0:
        return []
    tria = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(tria[i - 1][j - 1] + tria[i - 1][j])
        row.append(1)
        tria.append(row)
    return tria
