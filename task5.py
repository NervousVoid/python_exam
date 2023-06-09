
import math as m


def main(z):
    sum_i = 0
    n = len(z)
    for i in range(1, n + 1):
        sum_i += m.exp(81 - z[n - i] - z[n - i]**2)**7
    return sum_i
