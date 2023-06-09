
import math as m


def main(n):
    if n == 0:
        return -0.8
    return 62 * m.log10(main(n - 1) + 18 * main(n - 1)**2)**3
