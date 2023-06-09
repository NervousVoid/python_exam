import math as m


def main(y):
    numer = 90 * m.log10(56 * y * y + 1 + 67 * y * y * y)**7
    denom = 402 * y * y - (y * y - 23 - 94 * y * y * y)**4
    res = numer / denom + m.sqrt(y ** 5 + (m.sqrt(1 + y * y)**7))
    # return "{:.2e}".format(res)
    return res

main(0.91)
