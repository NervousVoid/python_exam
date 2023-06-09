
import math


def main(a, y, b, n, m):
    sum_k = 0
    for k in range(1, a + 1):
        sum_k += 32 * y**7 - 97 * k**5 - math.atan(94 * y - 4 - k**3)**2
    for k in range(1, m + 1):
        sum_c = 0
        for c in range(1, n + 1):
            sum_i = 0
            for i in range(1, b + 1):
                sum_i += i * i - 2 * (k * k - 7 * c**3)**5
            sum_c += sum_i
        sum_k += sum_c
    return sum_k
