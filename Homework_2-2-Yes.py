import math


def main(z):
    if z < 34:
        return pow(z, 4) - pow((57 + pow(z, 2) + 79 * pow(z, 3)), 6)
    elif z == 34 or z < 105:
        return pow(math.log2(21 * pow(z, 3) - pow(z, 2) - 0.5), 6) \
                + 83 * pow(z, 7) + pow((45 * z + pow(z, 3) + 1), 5)
    elif z == 105 or z < 176:
        return 27 * z + pow((z + 86), 6) + 21 * pow(z, 5)
    return 72 * pow(z, 3)
