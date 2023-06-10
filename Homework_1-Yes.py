import math


def main(x, y, z):
    a1 = 76 * (6 * z ** 3 - x - 1)
    a2 = y ** 2
    a3 = math.sqrt(a2 - a1)
    b1 = 82 * x - 1 - 23 * z ** 2
    b2 = math.exp(b1) ** 7
    c = 12 * math.log(y)
    d = a3 + b2 - c
    return d


print(main(-0.6, 0.08, 0.35))  # 3.36e+01
print(main(-0.9, 0.59, -0.54))  # 1.53e+01
print(main(-0.52, 0.7, -0.12))  # 1.04e+01
print(main(-0.45, 0.52, -0.07))  # 1.43e+01
print(main(-0.59, 0.15, -0.85))  # 4.04e+01
print(main(0.86, 0.99, -0.99))