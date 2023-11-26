#!/usr/bin/python3

"""
multiple two matrix
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrix
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if len(set([len(row) for row in m_a])) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set([len(row) for row in m_b])) != 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for r_i in range(len(m_b)):
                result[i][j] += m_a[i][r_i] * m_b[r_i][j]
    return result
