import math
import sys


def calcular(a, b):
    x = a+b
     y = a*b
       if (x > 10):
            print("Mayor a 10")
        else:
            print("Menor o igual a 10")
        return (x, y)


print(calcular(5, 8))
