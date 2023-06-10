import math


def main(a, m, b):
    res_sum = 0
    res_mul = 1
    for i in range(1, b + 1):
        res_sum += res_mul
        for j in range(1, m + 1):
            res_mul *= res_sum
            for c in range(1, a + 1):
                res_sum += j + (pow(i, 6) / 85) + pow(c, 5)

    return res_sum


print(main(7, 8, 5)) #2.80e+36
print(main(5, 6, 7)) #2.35e+24
print(main(8, 6, 5)) #2.90e+29
print(main(7, 6, 8)) #2.47e+28
print(main(5, 7, 8)) #1.25e+30
