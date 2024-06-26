#!/usr/bin/python3
"""
here comes the pascals triangle
"""


def pascal_triangle(n):
    """

    :param n: number of times to interate
    :return: list of list of intergers
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
