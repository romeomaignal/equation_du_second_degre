# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import math


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def doMath(a, b, c):
    alpha = -b / (2 * a)
    beta = -1 * ( b ** 2 - 4 * a * c ) / ( 4 * a )

    return alpha, beta

def equation_du_second_degre(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return x1, x2
    elif delta == 0:
        x0 = -b / (2 * a)
        return x0
    else:
        return 'l\'equation n\'admet aucune  solution dans R'

    

